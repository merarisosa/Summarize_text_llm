import logging
import os

base_path = os.getcwd()  
log_file_path = os.path.join(base_path, "utils", "logs", "app.log")

logging.basicConfig(     
    level=logging.DEBUG,     
    format="%(asctime)s - %(levelname)s - %(message)s",     
    handlers=[         
        logging.FileHandler(log_file_path, mode='w'),         
        logging.StreamHandler()     
    ] 
)
