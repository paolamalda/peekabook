# Íconos de cada mosaico (nombres de Font Awesome 4, los que usa el formato Mosaicos). Uno por parte, en orden,
# más los tres mosaicos comunes. Si un nombre no aparece en el selector de Mosaicos, se usa el más parecido.
COMUNES = [("Materiales de apoyo", "Support materials", "book", "libro"),
           ("Cierre y constancia", "Closing and certificate", "flag-checkered", "bandera de meta"),
           ("Programas y apoyos (extra)", "Programs and support (extra)", "life-ring", "salvavidas")]
D = {"wallet": ("money", "billetes"), "bank": ("university", "edificio de banco"), "card": ("credit-card", "tarjeta"), "shield": ("shield", "escudo"),
     "home": ("home", "casa"), "future": ("hourglass-half", "reloj de arena"), "calc": ("calculator", "calculadora"), "chart": ("line-chart", "gráfica de línea"),
     "cart": ("shopping-cart", "carrito"), "doc": ("file-text-o", "documento"), "grow": ("rocket", "cohete"), "swap": ("exchange", "flechas de intercambio"),
     "phone": ("mobile", "celular"), "warn": ("exclamation-triangle", "señal de alerta"), "lock": ("lock", "candado"), "health": ("heartbeat", "pulso"),
     "plan": ("list-alt", "lista"), "brief": ("briefcase", "portafolio"), "deal": ("handshake-o", "apretón de manos"), "scale": ("balance-scale", "balanza"),
     "bars": ("bar-chart", "gráfica de barras"), "unlock": ("unlock", "candado abierto"), "cal": ("calendar", "calendario"), "users": ("users", "grupo de personas"),
     "call": ("phone", "teléfono"), "star": ("star", "estrella"), "idea": ("lightbulb-o", "foco"), "pct": ("percent", "porcentaje"), "globe": ("globe", "globo terráqueo"),
     "compass": ("compass", "brújula"), "id": ("id-card", "credencial"), "tree": ("tree", "árbol"), "heart": ("heart", "corazón"), "umbrella": ("umbrella", "paraguas"),
     "folder": ("folder-open", "carpeta"), "plane": ("plane", "avión"), "moto": ("motorcycle", "motocicleta"), "amb": ("ambulance", "ambulancia"),
     "plus": ("plus-square", "cruz de salud"), "pen": ("pencil", "lápiz"), "hand": ("hand-paper-o", "mano de alto"), "child": ("child", "niña o niño"), "venus": ("venus", "símbolo femenino")}
NEG = ["swap", "calc", "chart", "cart", "doc", "card", "shield", "grow", "future"]
REG = ["id", "bank", "card", "plane", "future", "cal", "brief", "shield"]
CURSOS = {
 "tu_dinero_es": ["wallet", "bank", "card", "shield", "home"], "your_money_en": ["wallet", "bank", "card", "shield", "home"],
 "tu_negocio_mx": NEG, "tu_negocio_us_es": NEG, "your_business_us_en": NEG, "tu_regreso": REG, "back_home_en": REG,
 "tu_patrimonio": ["wallet", "bank", "phone", "warn", "lock", "chart", "future", "health", "doc", "home", "plan"],
 "tu_talento": ["wallet", "brief", "deal", "bank", "scale", "card", "bars", "unlock", "warn", "shield", "future"],
 "tu_turno": ["cal", "bank", "doc", "users", "bars", "call", "health", "future"],
 "tu_trabajo_hogar": ["wallet", "star", "users", "deal", "unlock", "health", "phone", "home", "chart"],
 "tu_idea": ["idea", "phone", "grow", "chart", "pct", "card", "shield", "globe", "compass"],
 "tu_comunidad": ["id", "bank", "swap", "users", "call", "tree", "heart"],
 "tu_costa": ["umbrella", "folder", "cal", "shield", "card", "scale", "swap", "home"],
 "tu_pension": ["cal", "card", "call", "hand", "wallet", "deal", "doc", "health"],
 "tu_ruta": ["wallet", "scale", "plus", "doc", "moto", "amb", "warn", "future"],
 "tu_temporada": ["pen", "home", "wallet", "swap", "doc", "shield", "cal", "future"],
 "tu_autonomia": ["id", "calc", "future", "venus", "umbrella", "hand", "child", "health"],
}


def tabla(curso, nombres, en=False):
    """Tabla markdown de íconos para el README; '' si el curso no tiene íconos definidos."""
    ks = CURSOS.get(curso)
    if not ks: return ""
    assert len(ks) == len(nombres), (curso, len(ks), len(nombres))
    h = ("| Tile | Icon | What it shows |\n|---|---|---|\n" if en else "| Mosaico | Ícono | Qué se ve |\n|---|---|---|\n")
    filas = [f"| {n} | `{D[k][0]}` | {D[k][1]} |" for n, k in zip(nombres, ks)]
    filas += [f"| {(ce if en else cs)} | `{i}` | {d} |" for cs, ce, i, d in COMUNES]
    return h + "\n".join(filas)
