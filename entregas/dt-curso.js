/* DT-CURSO: portada de cursos en Mosaicos de la categoría Desarrolla Talento.
   Se pega dentro de <script> en Administración del sitio > Apariencia > HTML adicional > "Antes de cerrar BODY".
   - Avance general: "83% · 52 de 63 lecciones" + botón "Continuar donde me quedé".
   - Contorno de los temas: terminado (rosa), en curso (rosa punteado), el que sigue (azul).
   No cambia datos: solo lee el avance que Moodle ya tiene. */
(function () {
  var b = document.body;
  if (!b || !b.classList.contains('format-tiles') || !b.classList.contains('category-8') ||
      !b.classList.contains('path-course-view')) { return; }
  var m = b.className.match(/course-(\d+)/);
  if (!m) { return; }
  var courseid = parseInt(m[1], 10);

  function pct(tile) {
    var t = tile.querySelector('.progress-indic.percent svg text');
    if (tile.querySelector('.tileallcomplete') && getComputedStyle(tile.querySelector('.tileallcomplete')).display !== 'none') { return 100; }
    return t ? parseInt(t.textContent, 10) || 0 : null;
  }

  function marcarTemas() {
    var tiles = Array.prototype.slice.call(document.querySelectorAll('ul.tiles > li.tile-clickable:not(.tile-hidden)'));
    var temas = tiles.slice(0, Math.max(0, tiles.length - 3));
    var actual = -1;
    temas.forEach(function (t, i) {
      t.classList.remove('dt-hecho', 'dt-encurso', 'dt-sigue');
      var p = pct(t);
      if (p === 100) { t.classList.add('dt-hecho'); } else if (actual < 0 && p !== null) { actual = i; }
    });
    if (actual >= 0) {
      temas[actual].classList.add('dt-encurso');
      if (temas[actual + 1] && !temas[actual + 1].classList.contains('dt-hecho')) { temas[actual + 1].classList.add('dt-sigue'); }
    }
  }

  function esc(x) { var d = document.createElement('div'); d.textContent = x || ''; return d.innerHTML.replace(/"/g, '&quot;'); }

  function barra(data) {
    if (document.getElementById('dt-avance')) { return; }
    var cont = document.querySelector('#page-header');
    if (!cont) { return; }
    var div = document.createElement('div');
    div.id = 'dt-avance';
    var txt = data.total ? (Math.round(100 * data.hechas / data.total) + '% · ' + data.hechas + ' de ' + data.total + ' lecciones') : '';
    var html = '';
    if (txt) {
      html += '<div class="dt-avance-txt"><span>Tu avance</span><strong>' + txt + '</strong>' +
        '<div class="dt-avance-barra"><i style="width:' + Math.round(100 * data.hechas / data.total) + '%"></i></div></div>';
    }
    if (data.url) {
      html += '<a class="dt-continuar" href="' + esc(data.url) + '"><span><b>▶</b>' + (data.hechas ? 'Continuar donde me quedé' : 'Comenzar el Tema 1') +
        '</span><small>' + esc(data.nombre) + '</small></a>';
    }
    if (!html) { return; }
    div.innerHTML = html;
    cont.appendChild(div);
  }

  function avance() {
    if (typeof require !== 'function') { return; }
    require(['core/ajax'], function (Ajax) {
      Ajax.call([{methodname: 'core_courseformat_get_state', args: {courseid: courseid}}])[0].then(function (r) {
        var st = JSON.parse(r);
        var secs = (st.section || []).filter(function (s) { return s.visible !== false; }).slice().sort(function (a, b) { return a.number - b.number; });
        var temas = secs.slice(1, Math.max(1, secs.length - 3));
        var cms = {};
        (st.cm || []).forEach(function (c) { cms[c.id] = c; });
        var total = 0, hechas = 0, sig = null, rastreado = false;
        temas.forEach(function (s) {
          (s.cmlist || []).forEach(function (id) {
            var c = cms[id];
            if (!c || c.module !== 'book' || c.visible === false) { return; }
            total++;
            if (c.istrackeduser) { rastreado = true; }
            var hecho = c.isoverallcomplete || (c.completionstate && c.completionstate > 0);
            if (hecho) { hechas++; } else if (!sig) { sig = c; }
          });
        });
        if (!rastreado) { return; }
        barra({total: total, hechas: hechas, url: sig ? sig.url : null, nombre: sig ? sig.name : ''});
      }).catch(function () {});
    });
  }

  function init() { marcarTemas(); avance(); }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); } else { init(); }
})();
