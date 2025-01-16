

def template_user_meeting_summary(text: str):
    template = f"""
        Por favor, resume la siguiente reunión y proporciona la salida en formato JSON. Utiliza esta estructura:  

    ```json
    {{ 
    "titulo": "[Título de la reunión o 'No especificado']",
    "fecha_hora": "[Fecha y hora de la reunión o 'No especificado']",
    "participantes": ["[Lista de participantes o 'No especificado']"],
    "temas_tratados": ["[Lista de los puntos discutidos o 'No especificado']"],
    "acuerdos_decisiones": ["[Lista de acuerdos alcanzados o 'No especificado']"],
    "tareas_pendientes": [
        {
        "descripcion": "[Descripción de la tarea o 'No especificado']",
        "responsable": "[Nombre del responsable o 'No especificado']",
        "plazo": "[Plazo o 'No especificado']"
        }
    ],
    "proxima_reunion": {
        "fecha_hora": "[Fecha y hora de la próxima reunión o 'No especificado']",
        "proposito": "[Propósito de la próxima reunión o 'No especificado']"
    }
    }}

    **Texto de la reunión**: "{text}"
    """
    return template
