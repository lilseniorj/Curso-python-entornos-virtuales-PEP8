# main.py - Todo el código en un archivo
"""
Sistema de análisis de noticias con APIs múltiples.
"""

# PEP 8: Configuración centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "es"  # PEP 8: Comillas dobles para strings


# PEP 8: Utilidades comunes del proyecto - funciones en snake_case
def clean_text(text):
    # PEP 8: 4 espacios por indentación, no tabs
    """Limpia y normaliza texto."""  # PEP 8: Docstrings en comillas dobles triples
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Doble líneas en blanco entre funciones para separar lógicamente
def validate_api_key(api_key):
    """Valida que la API key tenga formato correcto."""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Funciones principales - agrupadas después de utilidades
def fetch_news_from_api(api_name, query):
    """Obtiene noticias de una API específica."""
    pass


def process_article_data(raw_data):
    """Procesa datos crudos de artículo."""
    pass


# Longitud de línea: Máximo 88 caracteres (Ruff default)
# Indentación: 4 espacios, nunca tabs
# Nombres descriptivos: snake_case para funciones y variables
# Imports ordenados: estándar → terceros → locales
# Líneas en blanco: Separar funciones y clases lógicamente
# Comillas consistentes: Usar comillas dobles para strings



def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian: {section} desde {from_date} con Timeout: {timeout}, Retries: {retries}"


def ejemplo_args(api_key, *args):
    print(f"API Key: {api_key}")
    print(f"Args {args}")
    print(f"Type Args:{type(args)}")
    print("===========")

# ejemplo_args("API Key", "Este", "parametro", "aca")
# ejemplo_args("API Key", "Hola", "mundo")



"""Funcion para la suma de los parametros variables"""

def suma_numeros(*args):
    return sum(args)

# print(suma_numeros(1, 2, 3))          # Salida: 6
# print(suma_numeros(10, 20, 30, 40))  # Salida: 100




# Kwargs: Argumentos con nombre - diccionario de parámetros

def ejemplo_kwargs(**kwargs):
    print(f"kwargs: {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    print("======")


# ejemplo_kwargs(
#     api_key="DEMO",
#     query="Noticias de Python",
#     timeout=30,
#     retries=3,
# )
# ejemplo_kwargs(
#     api_key="DEMO_GUARDIAN",
#     section="Sports",
#     from_date="2020-10-20",
#     timeout=30,
#     retries=3,
# )


API_KEY = "434d64c5a1394492ab79df28239cd86c"
BASE_URL = "https://newsapi.org/v2/everything"

import json
import urllib.request
import urllib.parse


def newsapi_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"

    with urllib.request.urlopen(url, timeout=timeout) as response:
        data = response.read().decode("utf-8")
        return json.loads(data)
    return f"NewsAPI: {query}, con Timeout: {timeout}, Retries: {retries}"



def fetch_news(api_name, *args, **kwargs):
    """
    Fución flexible para conectar con la API
    """

    base_config = {
        "timeout": 30,
        "retries": 3,
    }

    config = {
        **base_config,
        **kwargs,
    }

    api_clients = {
        "newapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_clients[api_name]
    return client(*args, **config)

response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
for article in response_data["articles"]:
    print(article["title"])





