import time
import requests
import config
from utils.logs.filehandler import logging
import json

async def call_llama(template: str, system_template: str):
    try:
        start_time = time.time()
        
        payload = {
            "model": config.model_multimodal_name,  
            "prompt": template, 
            "system": system_template, 
            "stream": False, 
            }
        
        headers = {"Content-Type": "application/json"}
        response = requests.post(config.aws_model_url, json=payload, headers=headers)

        if response.status_code != 200:
            logging.error(f"Error en la respuesta del servicio. Código de estado: {response.status_code}")
            return {"error": "Error en la respuesta del servicio", "status_code": response.status_code}
        
        result = response.json()
        response_time = time.time() - start_time
        return {"response": result["response"], "response_time": response_time} 
    except requests.exceptions.RequestException as e:
        logging.error(f"Error en la solicitud HTTP: {str(e)}")
        return {"error": f"Error en la solicitud HTTP: {str(e)}", "status_code": 500}
    except Exception as e:
        logging.error(f"Error inesperado: {str(e)}")
        return {"error": str(e), "status_code": 500}