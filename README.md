# Resumidor de Textos con LLaMA (Local) 🚀

Este proyecto contiene una herramienta para resumir textos utilizando el modelo **LLaMA 3.2 Vision** de manera local. La aplicación es capaz de procesar texto plano y texto proveniente de varios tipos de documentos, generando resúmenes claros y concisos. Además, incluye plantillas específicas para resumir diferentes tipos de contenido, como **papers académicos**, **reuniones**, **correos electrónicos** y **resúmenes generales**.

## Características ✨

- **Resúmenes de texto plano**: Capacidad para generar resúmenes de textos simples de manera rápida y precisa.
- **Soporte para documentos**: Resumen de texto extraído de documentos como PDF, Word, y otros formatos compatibles.
- **Plantillas específicas**:
  - **Papers académicos**: Resúmenes que destacan los objetivos, metodología, resultados y conclusiones clave de investigaciones.
  - **Reuniones**: Resumen de las discusiones y decisiones tomadas durante una reunión, con tareas asignadas y próximos pasos.
  - **Correos electrónicos**: Resumen de la información clave de un email, incluyendo remitente, destinatario, asunto, contenido y acciones solicitadas.
  - **Resumen general**: Resúmenes breves y claros de cualquier tipo de contenido.

## Requisitos previos 🛠️

- **Python 3.x**: Asegúrate de tener Python instalado en tu sistema.
- **Dependencias**: Este proyecto usa varios paquetes de Python que se instalan automáticamente con `requirements.txt`.
- **LLaMA 3.2 Vision**: El modelo LLaMA debe estar configurado para su uso local.

## Instalación 📥

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/merarisosa/Summarize_text_llm.git
   cd summarize_api

2. **Construye el proyecto e inicialo**:
   ```bash
   python3 -m venv api/venv
   source api/venv/bin/activate
   docker-compose up --build

## Uso 📝

El resumen de texto se puede realizar de la siguiente manera:

   - **Resumir texto plano:**
        Puedes proporcionar cualquier texto para resumir directamente en Postman.

   - **Resumir documentos:**
        Extrae el texto de documentos (PDF, Word, Pptx, Img, etc.) y proporciona este texto para generar resúmenes.

   - **Seleccionar plantilla de resumen:**
        Elige la plantilla adecuada para resumir diferentes tipos de contenido, como papers académicos, reuniones, correos electrónicos o un resumen general.

## Estructura del Proyecto 📂

- **README.md:** Este archivo con la descripción del proyecto.
- **controller/:** Contiene los controladores que gestionan la lógica de las solicitudes y respuestas del sistema.
- **schema/:** Define la estructura de datos y los esquemas necesarios para la base de datos o los modelos utilizados.
- **functions/:** Contiene las funciones reutilizables para la implementación de la lógica de resumen y procesamiento de texto.
- **chroma/:** Base de datos en SQLite3 utilizada para almacenar las API keys.
- **repository/:** Funciones para interactuar con la base de datos, incluyendo operaciones de lectura y escritura.
- **router/:** Define las rutas de la API o endpoints que permiten interactuar con el sistema.
- **utils/:** Utilidades adicionales o funciones auxiliares que ayudan en tareas comunes, como el procesamiento de archivos o la gestión de configuraciones.
- **templates/:** Carpeta con plantillas específicas para cada tipo de resumen (por ejemplo, papers académicos, reuniones, correos electrónicos, etc.).
- **requirements.txt:** Lista de dependencias necesarias para el proyecto.

## Contribuciones 🤝

Las contribuciones son bienvenidas. Si tienes ideas para mejorar el proyecto o deseas agregar nuevas plantillas o funcionalidades, abre un issue o envía un pull request.
   
   
