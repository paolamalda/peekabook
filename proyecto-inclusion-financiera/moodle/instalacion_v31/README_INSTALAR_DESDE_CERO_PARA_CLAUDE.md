# Instrucciones para Claude: instalar el curso completo desde cero (Moodle 3.10)

Úsalo solo si el curso **todavía no existe** en la plataforma. Si ya existe, usa `README_ACTUALIZAR_CURSO_PARA_CLAUDE.md`.

Aplican las mismas reglas:

- Usa solo la interfaz web.
- No uses SSH.
- No instales complementos.
- No cambies la configuración del sitio.
- No toques otros cursos.

## 1. Crear el curso

*Administración del sitio > Cursos > Agregar un nuevo curso*:

| Campo | Valor |
|---|---|
| Nombre | Tu Dinero, Tu Familia, Tu Futuro (piloto California) |
| Nombre corto | TDTF-CA-ES |
| Visibilidad | **Ocultar** |
| Formato | Temas, 7 secciones |
| Seguimiento de finalización | Sí |

## 2. Secciones

| Sección | Nombre | Descripción |
|---|---|---|
| General | Bienvenida | Enlace al capítulo 1 del libro de apoyo y foro "Dudas y comentarios" |
| 1 | Módulo 1. Entiende tu dinero y organiza tu economía | contenido de `1_libros/M1_resumen.html` |
| 2 | Módulo 2. Entiende el sistema financiero y planea tus remesas | `M2_resumen.html` |
| 3 | Módulo 3. Construye tu crédito y maneja tus deudas | `M3_resumen.html` |
| 4 | Módulo 4. Protege tu dinero, tu identidad y tu familia | `M4_resumen.html` |
| 5 | Módulo 5. Construye patrimonio y prepara tu futuro | `M5_resumen.html` |
| 6 | Materiales de apoyo | "Casos, prácticas, glosario y dónde pedir ayuda." |
| 7 | Evaluación y constancia | "Tu constancia de conclusión." |

Descripción del foro "Dudas y comentarios": "No compartas números de cuenta, SSN, ITIN, contraseñas ni tu situación migratoria."

## 3. Contenido

Sigue los pasos 1 a 9 de `README_ACTUALIZAR_CURSO_PARA_CLAUDE.md`. Como no hay nada que borrar, en cada paso solo crea:

- libros;
- libro de apoyo;
- glosario;
- banco de preguntas y autoevaluaciones;
- actividades H5P;
- Level Up;
- insignias;
- finalización y constancia;
- revisión.

**Orden en cada sección de módulo:**

1. Libro.
2. Las actividades H5P de sus lecciones, en orden.
3. Autoevaluación.

## 4. Reporte

Entrega lo mismo que el paso 10 de la actualización, más el enlace del curso.
