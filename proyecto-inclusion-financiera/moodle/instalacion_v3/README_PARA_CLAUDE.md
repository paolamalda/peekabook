# Instrucciones para Claude: instalar el curso completo (formato v3) en Moodle 3.10

Vas a cargar "Tu Dinero, Tu Familia, Tu Futuro" en el Moodle de Desarrolla Talento. El sitio es academia.desarrollatalento.com, con Moodle 3.10, el tema Boost y Level Up 3.15.2.

Usa el navegador con la sesión de administrador que la persona abrió. Trabaja solo por la interfaz web.

Reglas:

- No uses SSH.
- No instales plugins.
- No cambies la configuración del sitio.
- No toques otros cursos.

## Antes de empezar

1. Pide la categoría del curso y la confirmación de que hay un respaldo reciente del sitio. Sin respaldo, detente.
2. Confirma la versión en *Administración del sitio > Notificaciones*. Si no es 3.10, avisa antes de seguir.

## Pasos

Sigue `LEEME.txt`, pasos 1 a 9, al pie de la letra. Datos clave:

- **Libros.** En cada libro usa *Importar capítulo* con el tipo "Cada archivo HTML representa un capítulo". Los archivos `*_sub.html` se vuelven subcapítulos automáticamente.
- **Formato de capítulo.** Usa "Nada".
- **Páginas esperadas.** Si el número no coincide, borra el libro y repite la importación.

  | Módulo | Capítulos | Páginas |
  |---|---|---|
  | M1 | 14 | 56 |
  | M2 | 13 | 52 |
  | M3 | 10 | 40 |
  | M4 | 11 | 44 |
  | M5 | 11 | 44 |

- **Glosario.** Hay uno solo: `2_glosario/Glosario_curso_Moodle.xml`.
- **No edites capítulos** con el editor de Moodle.

## Comprobaciones

Abre M1 U01 y M5 U10 con el rol de estudiante y revisa:

- La portada muestra dos botones de ruta.
- La navegación entre subcapítulos funciona.
- Los términos muestran su definición.
- Los bloques `<details>` abren y cierran.
- Los íconos Font Awesome se ven.

## Reporte final

Entrega a la persona:

- el enlace del curso;
- las páginas que se importaron por libro;
- lo que no se pudo hacer, y por qué;
- capturas de 2 lecciones.
