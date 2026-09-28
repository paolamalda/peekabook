# Guía de Level Up e insignias

Configuración propuesta para usar lo que ya tienes en Moodle: H5P, Level Up (block_xp) e insignias. El objetivo es motivar sin competir: los puntos premian constancia y práctica, no a quien sabe más.

## Principios

- **Sin tabla de clasificación pública con nombres.** Muchas personas participantes prefieren no mostrarse. Si activas el ranking, usa el modo anónimo o el que muestra solo a los vecinos cercanos.
- **Premiar terminar y practicar, no la calificación perfecta.**
- **Nada de puntos por tiempo en pantalla.** Premia completar.
- **Los niveles tienen nombres que cuentan un avance**, no rangos.

## Niveles (Level Up)

Configura 6 niveles, con los puntos acumulados que pide cada uno:

| Nivel | Nombre | Puntos acumulados |
|---|---|---|
| 1 | Empiezo | 0 |
| 2 | Me organizo | 300 |
| 3 | Uso mi cuenta | 800 |
| 4 | Cuido mi crédito | 1,400 |
| 5 | Protejo a mi familia | 2,100 |
| 6 | Construyo mi futuro | 2,900 |

## Reglas de puntos

| Acción | Puntos | Cómo se configura |
|---|---|---|
| Completar una lección (página o libro) | 20 | Regla por finalización de actividad* |
| Completar la actividad H5P | 20 | Finalización de actividad* |
| Aprobar el quiz de la lección (70% o más) | 20 | Finalización con calificación aprobatoria* |
| Entregar "A tu plan" (Tarea) | 30 | Evento "Entrega enviada" |
| Participar en el foro de dudas | 5 (máximo 3 al día) | Evento "Mensaje creado" con límite de repetición |
| Completar un módulo | 100 | Finalización de sección o regla de curso* |

\* Las reglas por finalización y calificación dependen de la versión instalada. La versión gratuita de Level Up asigna puntos por **eventos**, con reglas básicas. Las reglas por finalización de actividad, calificación y "bono de sección" son de **Level Up+**, que es de pago. **Por confirmar:** revisa en *Level Up > Reglas* qué opciones te aparecen.

**Si tienes la versión gratuita:** usa la regla por evento "Se ha completado el módulo del curso" (course_module_completion_updated), filtrada por el curso. La lista de eventos disponibles depende de tu versión.

**Evita el doble conteo:** desactiva los puntos por "ver" (course_module_viewed) o déjalos en 0, para que abrir y cerrar no dé puntos.

**Puntos estimados del curso completo:**

| Concepto | Cálculo | Puntos |
|---|---|---|
| Lección, H5P y quiz | 59 lecciones × 60 | 3,540 |
| "A tu plan" | 59 × 30 | 1,770 |
| Módulos | 5 × 100 | 500 |
| **Total** | | **5,810** |

Los niveles se alcanzan antes de terminar para que haya avance temprano. Ajusta los umbrales si ves que la mayoría se queda en un nivel.

## Insignias (Moodle, compatibles con Open Badges)

Crea las insignias en *Administración del curso > Insignias*. El criterio es la finalización de las actividades indicadas.

| Insignia | Criterio | Mensaje |
|---|---|---|
| Mi dinero en orden (M1) | Completar las 14 lecciones y el quiz de M1 | Organizaste tu calendario, presupuesto y carpeta fiscal. |
| Envío inteligente (M2) | Completar M2 | Sabes elegir cuenta y comparar remesas. |
| Crédito con rumbo (M3) | Completar M3 | Entiendes y cuidas tu crédito. |
| Familia protegida (M4) | Completar M4 | Tienes un plan de protección y respuesta. |
| Futuro en marcha (M5) | Completar M5 | Tu plan a largo plazo está escrito. |
| Detective de estafas | Aprobar H5P de M4 U01 y M3 U04 con 90% o más | Reconoces las señales de fraude. |
| Comparador experto | Completar H5P de M2 U04, M2 U08 y M3 U05 | Comparas con el costo total. |
| Plan completo | Las 5 insignias de módulo | Constancia de participación del programa. |

**Notas:**

- La insignia "Plan completo" acompaña la **constancia de participación**. No es un certificado ni una acreditación.
- En la descripción de cada insignia escribe las horas estimadas y las competencias trabajadas. Así sirve como evidencia en el expediente de impacto.
- Activa "Insignias en Mochila" (Open Badges) solo si las personas lo piden. Compartir es voluntario.

## Finalización de actividad (configuración base)

| Actividad | Condición de finalización |
|---|---|
| Página o libro de la lección | Ver |
| H5P no calificable | Ver |
| H5P calificable | Recibir calificación; aprobatoria 70% |
| Quiz de la lección | Calificación aprobatoria 70%, intentos ilimitados, mostrar retroalimentación al terminar |
| A tu plan (Tarea) | Enviar |

**Para el quiz:** importa `banco_preguntas_es.gift.txt` o `banco_preguntas_en.gift.txt` desde *Banco de preguntas > Importar > formato GIFT*. Se crean categorías por módulo (M1 a M5), con 3 preguntas por lección y 175 en total. Luego crea un cuestionario por lección con las 3 preguntas de esa lección.

## Datos para la evaluación de impacto

Exporta cada mes lo siguiente, sin nombres, con el ID interno de Moodle:

- Puntos y nivel por persona (Level Up > Informe).
- Insignias emitidas (Insignias > Destinatarios).
- Finalización por lección (Informes > Finalización de actividades).

Esto alimenta los indicadores E01 a E06 del plan maestro.
