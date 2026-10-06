# Programas y apoyos (módulo extra)

Los programas de gobierno y los servicios públicos **no van dentro de las lecciones**. Van en el libro extra «Programas y apoyos» de cada curso, en una sección aparte al final. Nada del curso depende de esa sección: se puede ocultar o borrar en Moodle sin afectar lecciones, finalización, puntos ni constancia.

## Cómo funciona

- Todo está en `programas.json`: un programa por entrada, con sus cursos, texto en español y en inglés, recurso oficial, fecha de revisión (`revisado`) y meses de vigencia (`vigencia_meses`, 6 por omisión).
- `python3 herramientas_cursos/curso.py cursos/<curso> programas` arma el libro solo con los programas vigentes. Si un programa pasa su vigencia sin revisarse, **queda fuera automáticamente** y se avisa en pantalla. Si un curso no tiene programas vigentes, no se genera el libro y el instructivo omite la sección.

## Para revisar un programa

1. Confirma en el sitio oficial que siga vigente y que los datos (montos, teléfonos, fechas) sean correctos.
2. Actualiza su texto y pon la fecha de hoy en `revisado`.
3. Regenera el libro y reemplaza en Moodle solo el libro «Programas y apoyos».

## Para quitar un programa

Bórralo de `programas.json` (o quita el curso de su lista) y regenera el libro.
