def template_user_papers_summary(text: str):
    template = f""" 
        Por favor, resume el siguiente paper académico y proporciona la salida en formato JSON. Asegúrate de seguir esta estructura:  

        ```json
        {{ 
        "titulo": "[Título del paper o 'No especificado']",
        "resumen": "[Resumen del paper con los puntos más importantes: objetivos, metodología, resultados y conclusiones]",
        "palabras_clave": ["[Lista de palabras clave extraídas del texto o 'No especificado']"]
        }}

        # Paper académico:
        **{text}**
    """
    return template
