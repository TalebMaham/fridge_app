import os
from dotenv import load_dotenv

load_dotenv()  # Charge les variables depuis le fichier .env

class Config:
    API_URL = os.getenv('API_URL')
    API_USERNAME = os.getenv('API_USERNAME')
    API_PASSWORD = os.getenv('API_PASSWORD')
