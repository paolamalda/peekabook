# Traspaso a la sesión local (instalación en Moodle)

Esta sesión corre en la computadora de la responsable del proyecto, con terminal y con Claude en Chrome.
Ella es quien decide; tú instalas, corriges y reportas en el mismo chat. No hay otra sesión con quien coordinar.

## Dónde está todo

- Repositorio: github.com/paolamalda/peekabook, rama `claude/trusting-lamport-fbbhf4`. Trabaja y sube cambios ahí.
- Sitio: academia.desarrollatalento.com (Moodle 4.5, tema Boost, formatos Mosaicos (Tiles), Level Up, Certificado personalizado, H5P).
- Instrucciones generales: `entregas/LEEME_INSTALACION_FINAL.txt`.
- Apariencia de los mosaicos: `entregas/ESTILO_MOSAICOS.txt` (meta: verse como https://claude.ai/artifact/QZPZczaSKKxXUKNJiCBRmk).
- Paquetes por curso: `entregas/*_v1.0*.zip`. Instructivo de cada curso: `cursos/<curso>/instalacion/README_*.md`.
- Generador (si hay que corregir contenido): `python3 herramientas_cursos/curso.py cursos/<curso> <paso>`; pasos en `paso_*` de ese archivo, o `todo`.

## Estado

- Tu Dinero ya está instalado: curso id 43, nombre corto DT-DINERO-CA-ES, categoría del banco «Tu Dinero v1.0».
  Ya se aplicaron el color de Boost y los colores de Mosaicos (#0A3161 y #E4007C).
- Se ve mal comparado con la vista aproximada. **Primer trabajo:** aplicar `ESTILO_MOSAICOS.txt` en Tu Dinero,
  comparar con la vista aproximada, ajustar selectores y reportar con capturas. No sigas con otros cursos hasta que ella lo apruebe.
- Íconos que sí existen en Mosaicos 4.5: dollar, id-card-o, umbrella y life-buoy (no money, credit-card, shield ni life-ring).
- Pendientes de Tu Dinero:
  - fecha de cierre de la cohorte para los seguimientos a 30 y 90 días (pregúntala);
  - si la constancia diseñada se vuelve plantilla del sitio (pregunta);
  - revisar los H5P con rol de estudiante.
- Insignias: «Detective de estafas» va con M2 U11, M4 U01 y M4 U02; «Comparador experto» va con M2 U08, M3 U05 y M5 U05.
- Después siguen los otros 17 cursos y las 7 comunidades, en el orden del LEEME.

## Reglas que no se rompen

- Cambios de configuración del SITIO: solo con autorización expresa de ella. Ya autorizó: color de Boost, colores de Mosaicos y el SCSS de `ESTILO_MOSAICOS.txt`.
- Antes de borrar cursos o cualquier cosa: muestra la lista y espera su confirmación.
- Claves de inscripción: te las da ella; nunca las guardes en el repositorio.
- Todos los cursos son versión 1.0 (nunca se han ofertado). Nombres cortos DT-…, como en el LEEME.
- Textos:
  - Dí «programa de bienestar financiero» y «sin costo» (nunca «gratis»).
  - No recomiendes SOFIPO, SOCAP, SOFOM ni marcas; enseña a verificar (SIPRES).
  - No pidas datos personales.
  - Sin asesoría legal ni migratoria.
  - No afirmes que hay cursos en lenguas indígenas.
  - Usa «Repasa», no «Pruébate».
  - Nada de «con cariño»; reconoce el esfuerzo y la constancia. Firma: «Desarrolla Talento».
  - No supongas cómo vive cada persona.
  - Contacto: hola@desarrollatalento.com.
- Programas de gobierno: solo en la sección extra «Programas y apoyos», nunca dentro de las lecciones.
  Banco del Bienestar solo en cursos no urbanos.
- Colores solo de la marca: #0A3161, #061F40, #E4007C, #FF4FA8. Nada verde ni café.
- No pongas identificadores de modelo en archivos del repositorio. No abras solicitudes de cambios (PR) si no te lo pide.

## Cómo reportar

Por etapas, en el chat: qué hiciste, capturas, qué quedó distinto a lo pedido y qué necesitas de ella. Breve.
