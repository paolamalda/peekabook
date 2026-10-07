/* DT-TABLERO: pantalla de inicio del estudiante (Tablero, /my/).
   Agrega arriba un saludo y una tarjeta por curso con su avance y el botón «Continuar».
   Va en HTML adicional > Antes de cerrar BODY, junto a DT-CURSO. Solo lee datos de Moodle. */
(function () {
  var b = document.body;
  if (!b || b.id !== 'page-my-index') { return; }
  var css = '' +
    '#dt-inicio{background:linear-gradient(120deg,#061F40 0%,#0A3161 70%,#14427E 100%);border-radius:18px;padding:24px 26px;margin:0 0 22px;color:#fff;position:relative;overflow:hidden;}' +
    '#dt-inicio h2{color:#fff;font-weight:800;font-size:1.7rem;margin:0;}' +
    '#dt-inicio .dt-sub{color:#FF8CC6;font-weight:600;margin:4px 0 16px;}' +
    '#dt-inicio .dt-cursos{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px;}' +
    '#dt-inicio .dt-c{background:#fff;color:#061F40;border-radius:14px;padding:16px;display:flex;flex-direction:column;gap:8px;box-shadow:0 4px 14px rgba(0,0,0,.15);}' +
    '#dt-inicio .dt-c small{font-size:.72rem;font-weight:800;color:#E4007C;text-transform:uppercase;letter-spacing:.05em;}' +
    '#dt-inicio .dt-c b{font-family:"Bricolage Grotesque",Figtree,sans-serif;font-size:1.1rem;line-height:1.2;}' +
    '#dt-inicio .dt-barra{height:8px;border-radius:99px;background:#E5ECF6;overflow:hidden;}' +
    '#dt-inicio .dt-barra i{display:block;height:100%;background:#E4007C;border-radius:99px;}' +
    '#dt-inicio .dt-pct{font-size:.8rem;color:#56627A;font-weight:600;}' +
    '#dt-inicio a.dt-ir{margin-top:auto;align-self:flex-start;background:#0A3161;color:#fff;border-radius:99px;padding:8px 18px;font-weight:700;text-decoration:none;}' +
    '#dt-inicio a.dt-ir:hover{background:#E4007C;}' +
    '#dt-inicio .dt-vacio{background:rgba(255,255,255,.1);border-radius:14px;padding:16px;}' +
    '#dt-inicio .dt-vacio a{color:#fff;font-weight:800;text-decoration:underline;}' +
    'body#page-my-index:has(#dt-inicio) section.block_recentlyaccessedcourses{display:none !important;}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  function esc(x) { var d = document.createElement('div'); d.textContent = x == null ? '' : String(x); return d.innerHTML.replace(/"/g, '&quot;'); }

  function nombre() {
    var el = document.querySelector('.usermenu .userinitials, .usermenu img.userpicture');
    var t = el ? (el.getAttribute('title') || el.getAttribute('alt') || '') : '';
    t = t.replace(/^(Imagen de|Picture of)\s+/i, '').trim();
    return t ? t.split(/\s+/)[0] : '';
  }

  function pintar(cursos) {
    var main = document.querySelector('#region-main [role="main"], #region-main');
    if (!main || document.getElementById('dt-inicio')) { return; }
    var n = nombre();
    var html = '<h2>' + (n ? '¡Hola, ' + esc(n) + '!' : '¡Hola!') + '</h2>' +
      '<p class="dt-sub">Qué bueno verte. Sigue donde te quedaste, a tu ritmo.</p>';
    if (cursos.length) {
      html += '<div class="dt-cursos">' + cursos.map(function (c) {
        var p = c.hasprogress ? Math.round(c.progress || 0) : null;
        return '<div class="dt-c"><small>' + esc(c.coursecategory || 'Curso') + '</small><b>' + esc(c.fullname) + '</b>' +
          (p !== null ? '<div class="dt-barra"><i style="width:' + p + '%"></i></div><span class="dt-pct">' + p + '% completado</span>' : '') +
          '<a class="dt-ir" href="' + esc(c.viewurl) + '">' + (p ? 'Continuar' : 'Empezar') + '</a></div>';
      }).join('') + '</div>';
    } else {
      html += '<div class="dt-vacio">Todavía no estás inscrito en ningún curso. <a href="/">Conoce los programas</a> y entra con tu código de acceso.</div>';
    }
    var sec = document.createElement('section'); sec.id = 'dt-inicio'; sec.innerHTML = html;
    main.insertBefore(sec, main.firstChild);
  }

  function init() {
    if (typeof require !== 'function') { return; }
    require(['core/ajax'], function (Ajax) {
      Ajax.call([{methodname: 'core_course_get_enrolled_courses_by_timeline_classification',
        args: {classification: 'inprogress', limit: 12, offset: 0, sort: 'ul.timeaccess desc'}}])[0]
        .then(function (r) { pintar(r.courses || []); })
        .catch(function () {});
    });
  }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); } else { init(); }
})();
