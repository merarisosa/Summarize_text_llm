def template_user_general_summary(text: str):

    template = f""" 
    Por favor, genera un resumen del siguiente contenido en formato JSON. Utiliza esta estructura:  

        ```json
        {{ 
        "titulo": "[Título del contenido o 'No especificado']",
        "resumen": "[Texto resumido con los puntos clave, en un máximo de 300 palabras]",
        "palabras_clave": ["[Lista de términos clave relacionados con el contenido o 'No especificado']"]
        }}

    Texto: {text}
    """
    return template