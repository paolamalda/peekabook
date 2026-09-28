// Genera plan-maestro.md y plan-maestro.html a partir de plan-maestro.json
const fs = require('fs');
const path = require('path');
const dir = path.join(__dirname, '..', 'entregables');
const data = JSON.parse(fs.readFileSync(path.join(dir, 'plan-maestro.json'), 'utf8'));

// ---------- Markdown ----------
let md = `# Plan maestro del programa\n\nActualizado: ${data.actualizado}\n\n`;
md += `## Diferenciadores\n\n| ID | Grupo | Diferenciador | Qué significa | Cómo se logra |\n|---|---|---|---|---|\n`;
data.diferenciadores.forEach(d => { md += `| ${d.id} | ${d.grupo} | ${d.titulo} | ${d.detalle} | ${d.como} |\n`; });
md += `\n## Complementos (app)\n\n| ID | Fase | Complemento | Valor para la persona | Lecciones | Nota |\n|---|---|---|---|---|---|\n`;
data.complementos.forEach(c => { md += `| ${c.id} | ${c.fase} | ${c.titulo} | ${c.valor} | ${c.curso} | ${c.nota} |\n`; });
md += `\n## Competencia y referentes de mercado\n\n| Nombre | Tipo | Qué ofrece | Costo | Brecha frente a nosotros | Cómo lo usamos |\n|---|---|---|---|---|---|\n`;
data.competencia.forEach(c => { md += `| ${c.nombre} | ${c.tipo} | ${c.ofrece} | ${c.costo} | ${c.brecha} | ${c.uso} |\n`; });
md += `\n## Pendientes\n\n`;
[...new Set(data.todo.map(t => t.cat))].forEach(cat => {
  md += `### ${cat}\n\n`;
  data.todo.filter(t => t.cat === cat).forEach(t => { md += `- [ ] **${t.id}** ${t.tarea} *(Responsable: ${t.resp})*\n`; });
  md += `\n`;
});
fs.writeFileSync(path.join(dir, 'plan-maestro.md'), md);

// ---------- HTML ----------
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const html = `<title>Plan Tu Dinero, Tu Familia</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Source+Sans+3:wght@400;600&display=swap">
<style>
:root{
  --bg:#F5F7F4; --surface:#FFFFFF; --ink:#1C2A25; --muted:#5B6B64; --line:#D6E0DA;
  --accent:#1F5C4A; --accent-soft:#E3EFE9; --chip:#EEF3F0;
  --todo:#9A6B12; --todo-soft:#FBF1DC; --doing:#2B5FA6; --doing-soft:#E4EDF9; --done:#2E7D4F; --done-soft:#E2F2E8;
  color-scheme:light;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#111916; --surface:#18221E; --ink:#E4ECE8; --muted:#9DB0A7; --line:#2C3B35;
  --accent:#6CC3A2; --accent-soft:#1D3129; --chip:#1F2B26;
  --todo:#E3B25A; --todo-soft:#33280F; --doing:#8DB5EE; --doing-soft:#1B2A40; --done:#79CF9C; --done-soft:#17301F;
  color-scheme:dark;}}
:root[data-theme="dark"]{
  --bg:#111916; --surface:#18221E; --ink:#E4ECE8; --muted:#9DB0A7; --line:#2C3B35;
  --accent:#6CC3A2; --accent-soft:#1D3129; --chip:#1F2B26;
  --todo:#E3B25A; --todo-soft:#33280F; --doing:#8DB5EE; --doing-soft:#1B2A40; --done:#79CF9C; --done-soft:#17301F;
  color-scheme:dark;}
body{background:var(--bg);color:var(--ink);font:16px/1.55 "Source Sans 3",system-ui,sans-serif}
.wrap{max-width:1080px;margin:0 auto;padding-inline:20px;padding-block:28px 64px}
header h1{font:700 clamp(28px,4vw,40px)/1.1 "Bricolage Grotesque",system-ui,sans-serif;margin:0 0 6px;text-wrap:balance}
header p{margin:0;color:var(--muted);max-width:65ch}
nav{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0 20px;position:sticky;top:env(safe-area-inset-top,0px);background:var(--bg);padding-block:10px;z-index:2}
nav button{font:600 15px "Source Sans 3",sans-serif;border:1px solid var(--line);background:var(--surface);color:var(--ink);padding:8px 14px;border-radius:999px;cursor:pointer}
nav button[aria-selected="true"]{background:var(--accent);border-color:var(--accent);color:var(--bg)}
nav button:focus-visible,select:focus-visible,input:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
nav .count{font-variant-numeric:tabular-nums;opacity:.75;margin-left:4px}
.tools{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:16px}
.tools input,.tools select{font:15px "Source Sans 3",sans-serif;padding:8px 10px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink);min-width:0}
.tools input{flex:1 1 220px}
h2{font:700 22px/1.2 "Bricolage Grotesque",sans-serif;margin:28px 0 12px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}
.card h3{margin:0;font:600 17px/1.3 "Source Sans 3",sans-serif}
.card p{margin:0;color:var(--muted)}
.meta{display:flex;flex-wrap:wrap;gap:6px;font-size:13px}
.chip{background:var(--chip);border-radius:999px;padding:2px 9px;color:var(--muted);font-variant-numeric:tabular-nums}
.chip.acc{background:var(--accent-soft);color:var(--accent);font-weight:600}
.how{font-size:14px;border-top:1px dashed var(--line);padding-top:6px;margin-top:2px}
.tbl{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
table{border-collapse:collapse;width:100%;min-width:860px;font-size:14.5px}
th,td{text-align:left;vertical-align:top;padding:10px 12px;border-bottom:1px solid var(--line)}
th{font-weight:600;color:var(--muted);font-size:13px;text-transform:uppercase;letter-spacing:.04em;background:var(--chip)}
tr:last-child td{border-bottom:0}
td:first-child{font-weight:600}
.progress{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-bottom:10px;font-variant-numeric:tabular-nums}
.bar{flex:1 1 240px;height:10px;border-radius:999px;background:var(--chip);overflow:hidden;display:flex}
.bar span{display:block;height:100%}
.todo-cat{margin-top:22px}
.todo-cat h3{font:700 18px "Bricolage Grotesque",sans-serif;margin:0 0 8px}
.item{display:grid;grid-template-columns:auto 1fr auto;gap:12px;align-items:start;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin-bottom:8px}
.item .id{font:600 13px "Source Sans 3",sans-serif;color:var(--muted);font-variant-numeric:tabular-nums;padding-top:3px}
.item .txt small{display:block;color:var(--muted);margin-top:2px}
.item select{font:600 13px "Source Sans 3",sans-serif;border-radius:999px;padding:5px 8px;border:1px solid var(--line);cursor:pointer}
.s-pendiente{background:var(--todo-soft);color:var(--todo)}
.s-en_curso{background:var(--doing-soft);color:var(--doing)}
.s-hecho{background:var(--done-soft);color:var(--done)}
.item.done .txt{text-decoration:line-through;text-decoration-color:var(--muted);opacity:.75}
.note{font-size:14px;color:var(--muted);margin:6px 0 0}
@media (max-width:560px){.item{grid-template-columns:1fr}.item .id{padding:0}}
@media (prefers-reduced-motion:no-preference){.bar span{transition:width .3s ease}}
</style>
<div class="wrap">
<header>
  <h1>Tu Dinero, Tu Familia, Tu Futuro</h1>
  <p>Diferenciadores, complementos de la app, competencia y pendientes del programa gratuito de finanzas para migrantes. Actualizado: ${esc(data.actualizado)}.</p>
</header>
<nav role="tablist" aria-label="Secciones">
  <button role="tab" id="tab-dif" aria-selected="true" data-tab="dif">Diferenciadores<span class="count">${data.diferenciadores.length}</span></button>
  <button role="tab" id="tab-com" aria-selected="false" data-tab="com">Complementos<span class="count">${data.complementos.length}</span></button>
  <button role="tab" id="tab-cmp" aria-selected="false" data-tab="cmp">Competencia<span class="count">${data.competencia.length}</span></button>
  <button role="tab" id="tab-todo" aria-selected="false" data-tab="todo">Pendientes<span class="count" id="todo-count">${data.todo.length}</span></button>
</nav>
<main>
<section id="p-dif" role="tabpanel" aria-labelledby="tab-dif"></section>
<section id="p-com" role="tabpanel" aria-labelledby="tab-com" hidden></section>
<section id="p-cmp" role="tabpanel" aria-labelledby="tab-cmp" hidden></section>
<section id="p-todo" role="tabpanel" aria-labelledby="tab-todo" hidden></section>
</main>
</div>
<script id="data" type="application/json">${JSON.stringify(data).replace(/</g, '\\u003c')}</script>
<script>
const D = JSON.parse(document.getElementById('data').textContent);
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const groups = a => [...new Set(a)];

// Pestañas
const tabs = document.querySelectorAll('nav button');
function show(t){
  tabs.forEach(b => b.setAttribute('aria-selected', String(b.dataset.tab === t)));
  ['dif','com','cmp','todo'].forEach(k => document.getElementById('p-'+k).hidden = k !== t);
  try { localStorage.setItem('tab', t); } catch(e) {}
}
tabs.forEach(b => b.addEventListener('click', () => show(b.dataset.tab)));
const hashTab = location.hash.replace('#','');
let saved = null; try { saved = localStorage.getItem('tab'); } catch(e) {}
show(['dif','com','cmp','todo'].includes(hashTab) ? hashTab : (saved || 'dif'));

// Diferenciadores
(function(){
  const el = document.getElementById('p-dif');
  el.innerHTML = '<div class="tools"><input id="q-dif" type="search" placeholder="Buscar diferenciador" aria-label="Buscar diferenciador"></div><div id="dif-list"></div>';
  const render = q => {
    const f = D.diferenciadores.filter(d => (d.titulo+d.detalle+d.como+d.grupo).toLowerCase().includes(q));
    document.getElementById('dif-list').innerHTML = groups(f.map(d => d.grupo)).map(g =>
      '<h2>'+esc(g)+'</h2><div class="grid">' + f.filter(d => d.grupo === g).map(d =>
        '<article class="card"><div class="meta"><span class="chip">'+d.id+'</span></div><h3>'+esc(d.titulo)+'</h3><p>'+esc(d.detalle)+'</p><div class="how"><strong>Cómo:</strong> '+esc(d.como)+'</div></article>').join('') + '</div>').join('') || '<p class="note">Sin resultados.</p>';
  };
  render('');
  document.getElementById('q-dif').addEventListener('input', e => render(e.target.value.toLowerCase()));
})();

// Complementos
(function(){
  const el = document.getElementById('p-com');
  el.innerHTML = groups(D.complementos.map(c => c.fase)).map(f =>
    '<h2>'+esc(f)+'</h2><div class="grid">' + D.complementos.filter(c => c.fase === f).map(c =>
      '<article class="card"><div class="meta"><span class="chip">'+c.id+'</span><span class="chip acc">'+esc(c.fase)+'</span></div><h3>'+esc(c.titulo)+'</h3><p>'+esc(c.valor)+'</p><div class="how"><strong>Lecciones:</strong> '+esc(c.curso)+'<br><strong>Nota:</strong> '+esc(c.nota)+'</div></article>').join('') + '</div>').join('');
})();

// Competencia
(function(){
  const el = document.getElementById('p-cmp');
  el.innerHTML = '<div class="tools"><input id="q-cmp" type="search" placeholder="Buscar por nombre o tipo" aria-label="Buscar competencia"></div><div class="tbl"><table><thead><tr><th>Nombre</th><th>Tipo</th><th>Qué ofrece</th><th>Costo</th><th>Brecha frente a nosotros</th><th>Cómo lo usamos</th></tr></thead><tbody id="cmp-body"></tbody></table></div>';
  const render = q => {
    document.getElementById('cmp-body').innerHTML = D.competencia.filter(c => (c.nombre+c.tipo+c.ofrece).toLowerCase().includes(q)).map(c =>
      '<tr><td>'+esc(c.nombre)+'</td><td>'+esc(c.tipo)+'</td><td>'+esc(c.ofrece)+'</td><td>'+esc(c.costo)+'</td><td>'+esc(c.brecha)+'</td><td>'+esc(c.uso)+'</td></tr>').join('');
  };
  render('');
  document.getElementById('q-cmp').addEventListener('input', e => render(e.target.value.toLowerCase()));
})();

// Pendientes con estado compartido
const state = {};
let db = null, canWrite = true;
const LABEL = {pendiente:'Pendiente', en_curso:'En curso', hecho:'Hecho'};
function renderTodo(){
  const el = document.getElementById('p-todo');
  const filter = (document.getElementById('f-todo') || {}).value || 'todos';
  const n = D.todo.length;
  const c = {pendiente:0,en_curso:0,hecho:0};
  D.todo.forEach(t => c[state[t.id] || 'pendiente']++);
  const pct = k => (100*c[k]/n).toFixed(1)+'%';
  const head = '<div class="progress"><strong>'+c.hecho+' de '+n+' hechos</strong><div class="bar" aria-hidden="true"><span style="width:'+pct('hecho')+';background:var(--done)"></span><span style="width:'+pct('en_curso')+';background:var(--doing)"></span></div><span class="chip">En curso: '+c.en_curso+'</span><span class="chip">Pendientes: '+c.pendiente+'</span></div>'
   + '<div class="tools"><label for="f-todo">Mostrar</label><select id="f-todo"><option value="todos">Todos</option><option value="pendiente">Pendientes</option><option value="en_curso">En curso</option><option value="hecho">Hechos</option></select></div>'
   + (db ? '' : '<p class="note">El estado compartido no está disponible en esta vista; los cambios no se guardarán.</p>')
   + (db && !canWrite ? '<p class="note">Tienes acceso de lectura; pide acceso de colaborador para cambiar estados.</p>' : '');
  const body = groups(D.todo.map(t => t.cat)).map(cat => {
    const items = D.todo.filter(t => t.cat === cat && (filter === 'todos' || (state[t.id] || 'pendiente') === filter));
    if (!items.length) return '';
    return '<div class="todo-cat"><h3>'+esc(cat)+'</h3>' + items.map(t => {
      const s = state[t.id] || 'pendiente';
      return '<div class="item'+(s==='hecho'?' done':'')+'"><span class="id">'+t.id+'</span><div class="txt">'+esc(t.tarea)+'<small>Responsable: '+esc(t.resp)+'</small></div>'
        + '<select id="s-'+t.id+'" class="s-'+s+'" data-id="'+t.id+'" aria-label="Estado de '+t.id+'"'+(db && canWrite ? '' : ' disabled')+'>'
        + Object.keys(LABEL).map(k => '<option value="'+k+'"'+(k===s?' selected':'')+'>'+LABEL[k]+'</option>').join('') + '</select></div>';
    }).join('') + '</div>';
  }).join('');
  el.innerHTML = head + body;
  document.getElementById('f-todo').value = filter;
  document.getElementById('f-todo').addEventListener('change', renderTodo);
  el.querySelectorAll('select[data-id]').forEach(sel => sel.addEventListener('change', async e => {
    const id = e.target.dataset.id, v = e.target.value, prev = state[id] || 'pendiente';
    state[id] = v; renderTodo();
    try { await db.doc('estado/'+id).set({ s: v, t: new Date().toISOString() }); }
    catch(err){ state[id] = prev; if (err && err.code === 'invalid_argument') canWrite = false; renderTodo(); }
  }));
}
renderTodo();
(async () => {
  try {
    db = await window.claude?.use?.('db');
    if (!db) { renderTodo(); return; }
    const user = await window.claude.use('user');
    if (user && user.can) { const w = await user.can('data.write'); if (w === false) canWrite = false; }
    db.collection('estado').onSnapshot(snap => {
      snap.docs.forEach(d => { const v = d.data(); if (v && v.s) state[d.id] = v.s; });
      renderTodo();
    }, () => { db = null; renderTodo(); });
    renderTodo();
  } catch(e) { db = null; renderTodo(); }
})();
</script>
`;
fs.writeFileSync(path.join(dir, 'plan-maestro.html'), html);
console.log('ok');
