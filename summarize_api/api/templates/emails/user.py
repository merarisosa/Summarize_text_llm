def template_user_emails(correo: str):
    template = f"""
    Por favor, genera un resumen del siguiente correo electrónico en formato JSON. Utiliza esta estructura:  

        ```json
        {{ 
        "remitente": "[Correo o nombre del remitente o 'No especificado']",
        "destinatarios": ["[Lista de correos o nombres de los destinatarios o 'No especificado']"],
        "asunto": "[Asunto del correo o 'No especificado']",
        "fecha_hora": "[Fecha y hora del correo o 'No especificado']",
        "contenido_principal": "[Motivo del correo, información clave y acciones solicitadas, máximo 200 palabras]",
        "adjuntos": ["[Lista de nombres o descripciones de archivos adjuntos o 'No especificado']"]
        }}

        Correo Electrónico: "{correo}" """
    return template