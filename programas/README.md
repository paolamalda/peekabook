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

## Calendario de fechas

`fechas.json` guarda las fechas que conviene saber (eventos, plazos, operativos). Cada una aparece en el capítulo «Fechas que conviene saber» del libro extra y **desaparece sola** al día siguiente de su fecha `hasta`.

## Verificación y avisos

- `python3 herramientas_cursos/verificacion.py` genera `proyecto-inclusion-financiera/entregables/verificacion_datos.md` (y `.csv`): todos los datos vigentes de las lecciones, los programas y las fechas, con su fecha de consulta, la fecha límite para revisarlos y una casilla para marcar «confirmado».
- Al revisar un curso (`curso.py … verificar`) aparece un aviso si alguna lección tiene datos con más de 6 meses sin revisarse.
- `python3 herramientas_cursos/vencimientos.py 30` lista lo que vence en los próximos 30 días. Una tarea automática lo corre el día 1 de cada mes y manda el resumen.
