# Tu Dinero, Tu Familia, Tu Futuro

Programa gratuito de finanzas personales para migrantes. Piloto en California; después Texas, Illinois, Nueva York y Florida.

## Entregables (carpeta `entregables/`)

| Archivo | Qué es |
|---|---|
| `Manual_participante_ES_v2.1.docx` | Manual del participante, edición en español (59 lecciones, con "Para saber más") |
| `Participant_Manual_EN_v2.1.docx` | Manual del participante, edición en inglés (con "Learn more") |
| `matriz/Matriz_comparativa_v1.xlsx` | Matriz de 62 productos: bancos, cooperativas, neobancos, remesadoras, crédito, prepagadas |
| `matriz/matriz-productos.json` / `matriz.html` | Datos de la matriz y página interactiva |
| `Manual_operador_ES_v2.docx` | Manual del operador en español: evaluación, claves, métricas, matriz, estados, control de cambios |
| `Operator_Manual_EN_v2.docx` | Manual del operador en inglés |
| `Proposed_Endeavor_Brief_NIW.docx` | Propuesta para el abogado de inmigración (en inglés) |
| `prompts-app-complementos.md` | Prompts de back end, front end, administración e integraciones de la app |
| `plan-maestro.md` / `.json` / `.html` | Diferenciadores, complementos, competencia y pendientes |

## Recursos (carpeta `recursos/`)

- `Para_saber_mas_por_leccion.xlsx` y `para_saber_mas_moodle.csv`: 140 enlaces oficiales por lección, listos para cargar como recursos URL en Moodle.
- `catalogo_recursos.md`: 65 recursos gratuitos (FDIC, CFPB, FTC, IRS, SEC, FTB, DMV, CONDUSEF y otros).

## Fuentes editables

- `manual/es/` y `manual/en/`: una carpeta por idioma, un archivo por módulo.
- `operador/es/` y `operador/en/`: manual del operador y trazabilidad.

## Cómo regenerar los Word

```bash
node herramientas/md2docx.js salida.docx "Título" "Subtítulo" archivo1.md archivo2.md ...
node herramientas/build-plan.js   # regenera el plan maestro desde el JSON
python3 herramientas/para_saber_mas.py   # inserta "Para saber más" y genera el catálogo
python3 herramientas/matriz_datos.py && python3 herramientas/matriz_xlsx.py   # matriz (requiere openpyxl)
```

Requiere el paquete `docx` de npm. Para la edición en inglés, usa `TOC_TITLE=Contents`.
