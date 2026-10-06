# Genera el tablero de resultados (un solo HTML) que lee las respuestas exportadas de las encuestas de Moodle.
# Uso: python3 herramientas_cursos/tablero.py   → entregas/tablero/Tablero_resultados.html
# Todo corre en el navegador: los archivos no salen de la computadora. Solo muestra grupos de 5 respuestas o más.
import json, os
import encuesta

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURSOS = os.path.join(RAIZ, "cursos")


def catalogo():
    cat = {}
    for c in sorted(os.listdir(CURSOS)):
        f = os.path.join(CURSOS, c, "curso.json")
        if not os.path.exists(f): continue
        cfg = json.load(open(f, encoding="utf-8"))
        v, neg = cfg.get("encuesta"), cfg.get("negocio", False)
        if not v: continue
        S, E, H, D, F, U = encuesta.items(v, neg)
        it = [{"id": i, "dim": d, "txt": t, "ops": [{"p": p, "o": o} for p, o in ops]} for i, d, t, ops in S + E + H + D + F]
        cat[c] = {"titulo": cfg["titulo"], "en": v == "us_en", "items": it}
    return cat


HTML = r"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tablero de resultados</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
<style>
:root{--bg:#f6f8fb;--card:#fff;--ink:#16223a;--mut:#5a6478;--line:#dde3ee;--az:#0a3161;--ro:#e4007c;--r1:#c62828;--r2:#f0a500;--r3:#2e7d32}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0f1522;--card:#18212f;--ink:#e8edf6;--mut:#9aa6bb;--line:#2a3547;--az:#7fb0ff;--ro:#ff5fb0}}
:root[data-theme="dark"]{--bg:#0f1522;--card:#18212f;--ink:#e8edf6;--mut:#9aa6bb;--line:#2a3547;--az:#7fb0ff;--ro:#ff5fb0}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
main{max-width:1100px;margin:0 auto;padding:24px 16px 60px}h1{color:var(--az);margin:0 0 4px;font-size:26px}h2{color:var(--az);font-size:19px;margin:28px 0 10px}
.mut{color:var(--mut)}.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin:12px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
label{display:block;font-weight:600;margin:8px 0 4px}select,input[type=file]{width:100%;padding:8px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink)}
.big{font-size:34px;font-weight:700;color:var(--az)}.bar{display:flex;height:14px;border-radius:7px;overflow:hidden;background:var(--line);margin:6px 0}
.bar span{display:block;height:100%}table{width:100%;border-collapse:collapse;font-size:14px}th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--mut);font-weight:600}.num{text-align:right;white-space:nowrap}.warn{border-left:4px solid var(--r2)}.ok{border-left:4px solid var(--r3)}
button{background:var(--az);color:#fff;border:0;border-radius:8px;padding:9px 14px;font-weight:600;cursor:pointer}.tw{overflow-x:auto}
.pill{display:inline-block;padding:1px 8px;border-radius:10px;font-size:12px;background:var(--line)}
</style></head><body><main>
<h1>Tablero de resultados</h1>
<p class="mut">Programa de bienestar financiero · Lee las respuestas de las encuestas exportadas de Moodle. Los archivos se leen en tu navegador y no se envían a ningún lado. Solo se muestran grupos de 5 respuestas o más.</p>
<div class="card">
 <div class="grid">
  <div><label for="curso">Curso</label><select id="curso"></select></div>
  <div><label for="f_inicio">Encuesta de inicio</label><input type="file" id="f_inicio" accept=".csv,.xlsx,.xls,.ods"></div>
  <div><label for="f_final">Encuesta final</label><input type="file" id="f_final" accept=".csv,.xlsx,.xls,.ods"></div>
  <div><label for="f_s30">Seguimiento a 30 días</label><input type="file" id="f_s30" accept=".csv,.xlsx,.xls,.ods"></div>
  <div><label for="f_s90">Seguimiento a 90 días</label><input type="file" id="f_s90" accept=".csv,.xlsx,.xls,.ods"></div>
 </div>
 <p class="mut" style="margin-bottom:0">Cómo exportar: en cada encuesta (Retroalimentación), <em>Mostrar respuestas</em> &gt; <em>Descargar datos de la tabla como</em> CSV o Excel. Descarga también las respuestas anónimas.</p>
</div>
<div id="out"></div>
</main>
<script>
const CAT = __CAT__;
const MIN = 5, ETAPAS = [["inicio","Inicio"],["final","Final"],["s30","30 días"],["s90","90 días"]];
const $ = id => document.getElementById(id);
const norm = s => String(s ?? "").normalize("NFD").replace(/[̀-ͯ]/g,"").toLowerCase().replace(/\s+/g," ").trim();
const DATA = {};
for (const [k,v] of Object.entries(CAT)) $("curso").append(new Option(v.titulo + (v.en ? " (EN)" : ""), k));
$("curso").onchange = render;
for (const [k] of ETAPAS) $("f_"+k).onchange = e => leer(k, e.target.files[0]);

function leer(k, f){
  if(!f) return; const r = new FileReader();
  r.onload = ev => { try {
      const u8 = new Uint8Array(ev.target.result); let wb;
      if (/\.csv$/i.test(f.name)) { let txt;
        try { txt = new TextDecoder("utf-8", {fatal:true}).decode(u8); } catch(_) { txt = new TextDecoder("windows-1252").decode(u8); }
        wb = XLSX.read(txt.replace(/^\ufeff/, ""), {type:"string"}); }
      else wb = XLSX.read(u8, {type:"array"});
      const ws = wb.Sheets[wb.SheetNames[0]];
      DATA[k] = XLSX.utils.sheet_to_json(ws, {header:1, defval:"", raw:false});
    } catch(e){ DATA[k] = null; alert("No se pudo leer el archivo: " + e.message); }
    render(); };
  r.readAsArrayBuffer(f);
}
// localiza la fila de encabezados y la columna de cada pregunta (por etiqueta P1… o por el texto)
function columnas(rows, items){
  let best = {h:-1, map:{}};
  for (let h = 0; h < Math.min(rows.length, 15); h++){
    const map = {};
    rows[h].forEach((c, j) => { const n = norm(c);
      for (const it of items){ if (map[it.id] !== undefined) continue;
        const t = norm(it.txt).slice(0, 40);
        if (n === norm(it.id) || n.startsWith("(" + norm(it.id) + ")") || n.startsWith(norm(it.id) + " ") || (t && n.includes(t))) { map[it.id] = j; break; } } });
    if (Object.keys(map).length > Object.keys(best.map).length) best = {h, map};
  }
  return best;
}
function opciones(it, val){ // devuelve los índices de opción elegidos
  const v = norm(String(val).replace(/^\(\s*-?\d+\s*\)\s*/, ""));
  if (!v) return [];
  const exact = it.ops.findIndex(o => norm(o.o) === v); if (exact >= 0) return [exact];
  return it.ops.map((o,i) => [i, norm(o.o)]).filter(([i,o]) => o && v.includes(o)).sort((a,b)=>b[1].length-a[1].length)
    .reduce((acc,[i,o]) => acc.some(j => norm(it.ops[j].o).includes(o)) ? acc : acc.concat(i), []);
}
function analizar(rows, curso){
  const items = CAT[curso].items; const {h, map} = columnas(rows, items);
  if (h < 0 || !map.P1) return {error: "No se encontraron las preguntas del curso en el archivo. Revisa que sea la encuesta de este curso."};
  const resp = rows.slice(h+1).filter(r => r.some(c => String(c).trim()));
  const R = resp.map(r => { const o = {}; for (const it of items) if (map[it.id] !== undefined) o[it.id] = it.ops.length ? opciones(it, r[map[it.id]]) : String(r[map[it.id]]||"").trim(); return o; });
  const P = items.filter(i => i.dim !== "perfil" && i.ops.length && i.ops[0].p !== null && /^P\d/.test(i.id));
  for (const o of R){ const pts = P.map(it => o[it.id] && o[it.id].length ? it.ops[o[it.id][0]].p : null);
    o._idx = pts.every(x => x !== null) ? pts.reduce((a,b)=>a+b,0)/pts.length : null;
    o._sub = {}; for (const d of ["gastar","ahorrar","deber","planear"]){ const s = P.filter(i=>i.dim===d).map(i => o[i.id]&&o[i.id].length ? i.ops[o[i.id][0]].p : null); o._sub[d] = s.every(x=>x!==null) ? s.reduce((a,b)=>a+b,0)/s.length : null; } }
  return {R, items, n: R.length};
}
const prom = a => { const v = a.filter(x => x !== null && x !== undefined); return v.length ? v.reduce((x,y)=>x+y,0)/v.length : null; };
const nivel = x => x < 40 ? 0 : x < 80 ? 1 : 2;
const NIV = ["En riesgo (0–39)","Equilibrio frágil (40–79)","Con bienestar (80–100)"], COL = ["var(--r1)","var(--r2)","var(--r3)"];
const f1 = x => x === null ? "—" : x.toFixed(1);
function barra(parts){ const t = parts.reduce((a,b)=>a+b,0)||1; return `<div class="bar">${parts.map((p,i)=>`<span style="width:${100*p/t}%;background:${COL[i]}"></span>`).join("")}</div>`; }
function render(){
  const curso = $("curso").value, out = $("out"); const A = {};
  for (const [k] of ETAPAS) if (DATA[k]) A[k] = analizar(DATA[k], curso);
  if (!Object.keys(A).length){ out.innerHTML = `<div class="card mut">Carga al menos un archivo para ver resultados.</div>`; return; }
  let h = `<h2>Índice de bienestar financiero</h2><div class="grid">`;
  const resumen = [["Etapa","Respuestas","Índice","En riesgo %","Frágil %","Con bienestar %","Gastar","Ahorrar","Deber","Planear"]];
  for (const [k, nom] of ETAPAS){ const a = A[k]; if (!a) continue;
    if (a.error){ h += `<div class="card warn"><b>${nom}</b><br>${a.error}</div>`; continue; }
    const v = a.R.map(r=>r._idx).filter(x=>x!==null);
    if (v.length < MIN){ h += `<div class="card warn"><b>${nom}</b><br>${v.length} respuestas completas: se necesitan al menos ${MIN} para mostrar resultados.</div>`; continue; }
    const cnt = [0,0,0]; v.forEach(x => cnt[nivel(x)]++); const i = prom(v);
    const sub = ["gastar","ahorrar","deber","planear"].map(d => prom(a.R.map(r=>r._sub[d])));
    h += `<div class="card"><b>${nom}</b> <span class="pill">${v.length} respuestas</span><div class="big">${f1(i)}</div>${barra(cnt)}
      <div class="mut" style="font-size:13px">${NIV.map((n,j)=>`${n}: ${Math.round(100*cnt[j]/v.length)}%`).join(" · ")}</div>
      <table style="margin-top:8px">${["Gastar","Ahorrar","Deber","Planear"].map((d,j)=>`<tr><td>${d}</td><td class="num">${f1(sub[j])}</td></tr>`).join("")}</table></div>`;
    resumen.push([nom, v.length, f1(i), ...cnt.map(c=>Math.round(100*c/v.length)), ...sub.map(f1)]);
  }
  h += `</div>`;
  if (A.inicio && A.final && !A.inicio.error && !A.final.error){
    const a = prom(A.inicio.R.map(r=>r._idx)), b = prom(A.final.R.map(r=>r._idx));
    if (a !== null && b !== null && A.inicio.n >= MIN && A.final.n >= MIN)
      h += `<div class="card ok"><b>Cambio de inicio a final:</b> ${b-a >= 0 ? "+" : ""}${(b-a).toFixed(1)} puntos en el índice promedio. <span class="mut">Las encuestas son anónimas: se comparan grupos, no personas; quienes contestan al final pueden ser distintas de quienes contestaron al inicio.</span></div>`;
  }
  // perfil (solo inicio)
  if (A.inicio && !A.inicio.error){ for (const pid of ["D1","D2"]){ const it = A.inicio.items.find(i=>i.id===pid); if (!it) continue;
    const g = {}; A.inicio.R.forEach(r => { const o = r[pid]&&r[pid].length ? it.ops[r[pid][0]].o : "Sin respuesta"; (g[o] = g[o]||[]).push(r._idx); });
    let otros = []; const filas = [];
    for (const [o, v] of Object.entries(g)){ const vv = v.filter(x=>x!==null); if (vv.length >= MIN) filas.push([o, vv.length, prom(vv)]); else otros = otros.concat(vv); }
    if (otros.length >= MIN) filas.push(["Otros grupos (menores a 5, combinados)", otros.length, prom(otros)]);
    h += `<h2>Inicio por ${it.txt.replace(/\s*\(opcional\)|\s*\(optional\)/i,"").toLowerCase()}</h2><div class="card tw"><table><tr><th>Grupo</th><th class="num">Respuestas</th><th class="num">Índice</th></tr>${filas.map(f=>`<tr><td>${f[0]}</td><td class="num">${f[1]}</td><td class="num">${f1(f[2])}</td></tr>`).join("") || `<tr><td colspan=3 class="mut">Ningún grupo llega a ${MIN} respuestas.</td></tr>`}</table></div>`; } }
  // estrés, hábitos y programa
  for (const [dim, tit] of [["estres","Señales de estrés"],["habitos","Hábitos"],["programa","Evaluación del programa (final)"]]){
    const et = ETAPAS.filter(([k]) => A[k] && !A[k].error && A[k].n >= MIN && A[k].items.some(i=>i.dim===dim && A[k].R.some(r=>r[i.id]!==undefined)));
    if (!et.length) continue;
    h += `<h2>${tit}</h2>`;
    const base = A[et[0][0]].items.filter(i => i.dim === dim && i.ops.length);
    for (const it of base){
      const cols = et.filter(([k]) => A[k].R.some(r => r[it.id] !== undefined));
      h += `<div class="card tw"><b>${it.id}.</b> ${it.txt}<table><tr><th>Opción</th>${cols.map(([k,n])=>`<th class="num">${n} %</th>`).join("")}</tr>`;
      it.ops.forEach((o, j) => { h += `<tr><td>${o.o}</td>${cols.map(([k]) => { const rr = A[k].R.filter(r => r[it.id] && r[it.id].length); return `<td class="num">${rr.length >= MIN ? Math.round(100*rr.filter(r=>r[it.id].includes(j)).length/rr.length) : "—"}</td>`; }).join("")}</tr>`; });
      if (it.id === "F3"){ const rr = A.final ? A.final.R.filter(r=>r.F3&&r.F3.length).map(r=>+it.ops[r.F3[0]].o) : [];
        if (rr.length >= MIN){ const nps = Math.round(100*(rr.filter(x=>x>=9).length - rr.filter(x=>x<=6).length)/rr.length); h += `<tr><td colspan=${cols.length+1}><b>Recomendación neta:</b> ${nps} (de −100 a 100)</td></tr>`; } }
      h += `</table></div>`;
    }
  }
  h += `<p><button id="dl">Descargar resumen (CSV, sin respuestas individuales)</button></p>`;
  out.innerHTML = h;
  $("dl").onclick = () => { const csv = resumen.map(r => r.map(c => `"${String(c).replace(/"/g,'""')}"`).join(",")).join("\n");
    const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob(["﻿"+csv], {type:"text/csv"})); a.download = "resumen_" + curso + ".csv"; a.click(); };
}
render();
</script></body></html>
"""

if __name__ == "__main__":
    d = os.path.join(RAIZ, "entregas", "tablero"); os.makedirs(d, exist_ok=True)
    cat = catalogo()
    open(os.path.join(d, "Tablero_resultados.html"), "w", encoding="utf-8").write(HTML.replace("__CAT__", json.dumps(cat, ensure_ascii=False)))
    print("tablero:", len(cat), "cursos")
