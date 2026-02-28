"""Configuración de la aplicación."""
import os
from dotenv import load_dotenv

load_dotenv()

os.environ.get("API_KEY")

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"