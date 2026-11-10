PREGUNTAS = [
    {
        "id": 1,
        "texto": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Marte", "Júpiter", "Saturno", "Venus"],
        "respuesta_correcta": 1,
    },
    {
        "id": 2,
        "texto": "¿Cuál es la capital de Japón?",
        "opciones": ["Kioto", "Osaka", "Tokio", "Nagoya"],
        "respuesta_correcta": 2,
    },
    {
        "id": 3,
        "texto": "¿Quién escribió Don Quijote de la Mancha?",
        "opciones": [
            "Federico García Lorca",
            "Miguel de Cervantes",
            "Lope de Vega",
            "Benito Pérez Galdós",
        ],
        "respuesta_correcta": 1,
    },
    {
        "id": 4,
        "texto": "¿Qué elemento químico tiene el símbolo O?",
        "opciones": ["Oro", "Osmio", "Oxígeno", "Oliva"],
        "respuesta_correcta": 2,
    },
    {
        "id": 5,
        "texto": "¿En qué continente se encuentra Egipto?",
        "opciones": ["Asia", "Europa", "África", "Oceanía"],
        "respuesta_correcta": 2,
    },
]


def obtener_preguntas(
    cantidad: int = 5,
) -> list[dict[str, int | str | list[str]]]:
    return [
        {
            "id": pregunta["id"],
            "texto": pregunta["texto"],
            "opciones": pregunta["opciones"].copy(),
        }
        for pregunta in PREGUNTAS[:cantidad]
    ]


def responder(id_pregunta: int, opcion: int) -> dict[str, bool | int] | None:
    for pregunta in PREGUNTAS:
        if pregunta["id"] == id_pregunta:
            respuesta_correcta = pregunta["respuesta_correcta"]
            return {
                "correcta": opcion == respuesta_correcta,
                "respuesta_correcta": respuesta_correcta,
            }
    return None
