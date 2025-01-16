import os
from utils.logs.filehandler import logging
from dotenv import load_dotenv

load_dotenv() 

aws_model_url = os.getenv('AWS_MODEL_URL')
model_text_only_name = os.getenv('MODEL_TEXT_ONLY_NAME')
model_multimodal_name = os.getenv('MODEL_MULTIMODAL_NAME')

if not aws_model_url:
    logging.warning("AWS_MODEL_URL no está configurada.")
else:
    logging.info(f"Conectando al servicio Llama en: {aws_model_url}")
    logging.info(f"Modelo Lightweight {model_text_only_name}")
    logging.info(f"Modelo Multimodal {model_multimodal_name}")





