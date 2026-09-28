# Textos de la interfaz en inglés para build_v3.py --en (se aplican al HTML y al texto legible ya generados).
UI = {
 "Profundiza: casos, errores frecuentes y más datos": "Go deeper: cases, common mistakes and more facts",
 "Para cuando tienes poco tiempo o ya conoces el tema": "For when you are short on time or already know the topic",
 "La actividad está justo después de este libro, en la sección del módulo.": "The activity is right after this book, in the module section.",
 "Toca o pasa el cursor sobre cada palabra para ver qué significa.": "Tap or hover over each word to see what it means.",
 "Completa la actividad y el quiz para sumar puntos.": "Complete the activity and the quiz to earn points.",
 "Significado de los términos del curso, en palabras sencillas.": "What the course terms mean, in plain words.",
 "VISTA PREVIA · así se verá en el Libro de Moodle": "PREVIEW · how it will look in the Moodle Book",
 "| Tipo | Descripción | Qué significa para ti |": "| Type | Description | What it means for you |",
 "| Error | Qué pasa | Qué hacer |": "| Mistake | What happens | What to do |",
 "Lo esencial (5 minutos)": "The essentials (5 minutes)", "Profundiza (5 minutos más)": "Go deeper (5 more minutes)",
 "Casos: piensa y luego revisa": "Cases: think first, then check", "Comprueba lo que entendiste": "Check your understanding",
 "Profundizar (+5 min)": "Go deeper (+5 min)", "Volver a lo esencial": "Back to the essentials",
 "Pon a prueba lo que sabes": "Test what you know", "¡Terminaste esta lección!": "You finished this lesson!",
 "Lo esencial · 5 min": "The essentials · 5 min", "Profundiza · +5 min": "Go deeper · +5 min",
 "Actividad interactiva": "Interactive activity", "Errores frecuentes": "Common mistakes", "Ponlo en práctica": "Put it into practice",
 "Para entender a fondo": "To understand it fully", "Siguiente lección": "Next lesson", "Lo que lograrás": "What you will be able to do",
 "Para saber más": "Learn more", "Palabras clave": "Key words", "Para recordar": "Remember", "Elige tu ruta": "Choose your path",
 "Ruta rápida": "Quick path", "Ruta completa": "Full path", "En esta lección": "In this lesson", "Ir a practicar": "Go to practice",
 "Ver respuestas": "See answers", "Ver respuesta": "See answer", "Qué buscar:": "What to look for:", "Para empezar": "To start",
 "*Respuesta:*": "*Answer:*", "**Respuestas:**": "**Answers:**", "**Respuesta:**": "**Answer:**",
 "Lo esencial": "The essentials", "Profundiza": "Go deeper", "Practica": "Practice", "A tu plan": "Your plan", "Fuentes": "Sources",
 "Inicio": "Start", "#### Casos": "#### Cases",
}
TITLES = {"M1": "Module 1. Understand your money and organize your finances", "M2": "Module 2. Understand the financial system and plan your remittances",
          "M3": "Module 3. Build your credit and manage your debts", "M4": "Module 4. Protect your money, your identity and your family",
          "M5": "Module 5. Build wealth and prepare your future"}
def tr(s):
    for k in sorted(UI, key=len, reverse=True):
        s = s.replace(k, UI[k])
    return s
