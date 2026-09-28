// Convierte un subconjunto de Markdown a .docx (Word).
// Uso: node md2docx.js salida.docx "Título en portada" "Subtítulo" archivo1.md [archivo2.md ...]
// Soporta: # a ####, párrafos, listas "- " y "1. ", tablas con "|", **negrita**, *cursiva*,
// citas "> " (recuadro sombreado), "---" (salto de página) y [[TOC]] (índice).
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, LevelFormat, PageBreak,
  TableOfContents, Footer, PageNumber,
} = require('docx');

const [, , out, title, subtitle, ...files] = process.argv;
const PAGE_W = 12240, MARGIN = 1300, CONTENT_W = PAGE_W - 2 * MARGIN;
const ACCENT = '1F5C4A', SOFT = 'EAF2EE', BORDER = 'B7C9C0';

function runs(text, base = {}) {
  const parts = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) parts.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith('**')) parts.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
    else parts.push(new TextRun({ text: t.slice(1, -1), italics: true, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) parts.push(new TextRun({ text: text.slice(last), ...base }));
  return parts;
}

function cell(text, width, header) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: header ? { type: ShadingType.CLEAR, color: 'auto', fill: ACCENT } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: [new Paragraph({ children: runs(text, header ? { bold: true, color: 'FFFFFF', size: 18 } : { size: 18 }) })],
  });
}

function table(rows) {
  const data = rows.filter(r => !/^\|\s*:?-{2,}/.test(r)).map(r =>
    r.replace(/^\||\|$/g, '').split('|').map(c => c.trim()));
  const n = data[0].length;
  const w = Math.floor(CONTENT_W / n);
  const widths = Array(n).fill(w);
  widths[n - 1] = CONTENT_W - w * (n - 1);
  const b = { style: BorderStyle.SINGLE, size: 4, color: BORDER };
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    borders: { top: b, bottom: b, left: b, right: b, insideHorizontal: b, insideVertical: b },
    rows: data.map((r, i) => new TableRow({
      tableHeader: i === 0,
      children: widths.map((wd, j) => cell(r[j] || '', wd, i === 0)),
    })),
  });
}

let listInstance = 0;
function convert(md) {
  const out = [];
  let inNumbered = false;
  const lines = md.replace(/\r/g, '').split('\n');
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    const t = line.trim();
    if (!t) { i++; continue; }
    if (!/^\d+\.\s+/.test(t)) inNumbered = false;
    if (t === '[[TOC]]') {
      out.push(new TableOfContents(process.env.TOC_TITLE || 'Contenido', { hyperlink: true, headingStyleRange: '1-2' }));
      i++; continue;
    }
    if (t === '---') { out.push(new Paragraph({ children: [new PageBreak()] })); i++; continue; }
    const h = /^(#{1,4})\s+(.*)$/.exec(t);
    if (h) {
      const lvl = [HeadingLevel.HEADING_1, HeadingLevel.HEADING_2, HeadingLevel.HEADING_3, HeadingLevel.HEADING_4][h[1].length - 1];
      out.push(new Paragraph({ heading: lvl, children: runs(h[2]) }));
      i++; continue;
    }
    if (t.startsWith('|')) {
      const rows = [];
      while (i < lines.length && lines[i].trim().startsWith('|')) rows.push(lines[i].trim()), i++;
      out.push(table(rows));
      out.push(new Paragraph({ children: [] }));
      continue;
    }
    if (t.startsWith('> ')) {
      const buf = [];
      while (i < lines.length && lines[i].trim().startsWith('>')) buf.push(lines[i].trim().replace(/^>\s?/, '')), i++;
      buf.filter(x => x).forEach((x, k, arr) => out.push(new Paragraph({
        shading: { type: ShadingType.CLEAR, color: 'auto', fill: SOFT },
        border: { left: { style: BorderStyle.SINGLE, size: 18, color: ACCENT, space: 8 } },
        indent: { left: 200, right: 200 },
        spacing: { before: k === 0 ? 120 : 0, after: k === arr.length - 1 ? 160 : 40 },
        children: runs(x),
      })));
      continue;
    }
    const bl = /^[-*]\s+(.*)$/.exec(t);
    if (bl) {
      const depth = (line.match(/^\s*/)[0].length >= 2) ? 1 : 0;
      out.push(new Paragraph({ numbering: { reference: 'bullets', level: depth }, children: runs(bl[1]) }));
      i++; continue;
    }
    const nl = /^\d+\.\s+(.*)$/.exec(t);
    if (nl) {
      if (!inNumbered) { listInstance++; inNumbered = true; }
      out.push(new Paragraph({ numbering: { reference: 'numbers', level: 0, instance: listInstance }, children: runs(nl[1]) }));
      i++; continue;
    }
    // Párrafo: une líneas consecutivas
    const buf = [t];
    i++;
    while (i < lines.length && lines[i].trim() && !/^(#|\||>|[-*]\s|\d+\.\s|---|\[\[TOC\]\])/.test(lines[i].trim())) buf.push(lines[i].trim()), i++;
    out.push(new Paragraph({ children: runs(buf.join(' ')) }));
  }
  return out;
}

const body = [];
body.push(new Paragraph({ spacing: { before: 2400 }, children: [] }));
body.push(new Paragraph({ alignment: AlignmentType.LEFT, children: [new TextRun({ text: title, bold: true, size: 52, color: ACCENT })] }));
if (subtitle) body.push(new Paragraph({ spacing: { before: 200 }, children: [new TextRun({ text: subtitle, size: 28, color: '44544D' })] }));
body.push(new Paragraph({ children: [new PageBreak()] }));
files.forEach((f, k) => {
  body.push(...convert(fs.readFileSync(f, 'utf8')));
  if (k < files.length - 1) body.push(new Paragraph({ children: [new PageBreak()] }));
});

const doc = new Document({
  creator: 'Desarrolla Talento',
  title,
  features: { updateFields: true },
  styles: {
    default: { document: { run: { font: 'Calibri', size: 22 }, paragraph: { spacing: { after: 120, line: 300 } } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 36, bold: true, color: ACCENT }, paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 28, bold: true, color: '23433A' }, paragraph: { spacing: { before: 300, after: 140 }, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 24, bold: true, color: ACCENT }, paragraph: { spacing: { before: 220, after: 100 }, outlineLevel: 2 } },
      { id: 'Heading4', name: 'Heading 4', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 22, bold: true, color: '44544D' }, paragraph: { spacing: { before: 160, after: 80 }, outlineLevel: 3 } },
    ],
  },
  numbering: {
    config: [
      { reference: 'bullets', levels: [
        { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } },
        { level: 1, format: LevelFormat.BULLET, text: '◦', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1000, hanging: 270 } } } },
      ] },
      { reference: 'numbers', levels: [
        { level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 300 } } } },
      ] },
    ],
  },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: 15840 }, margin: { top: 1300, bottom: 1300, left: MARGIN, right: MARGIN } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, color: '6B7A73' })] })] }) },
    children: body,
  }],
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(out, b); console.log('OK', out); });
