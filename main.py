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



def newapi_client(api_key, query, timeout=30, retries=3):
    return f"NewsAPI: {query}, con Timeout: {timeout}, Retries: {retries}"

def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian: {section} desde {from_date} con Timeout: {timeout}, Retries: {retries}"

def ejemplo_args(api_key, *args):
    print(f"API Key: {api_key}")
    print(f"Args {args}")
    print(f"Type Args:{type(args)}")
    print("===========")

ejemplo_args("API Key", "Este", "parametro", "aca")
ejemplo_args("API Key", "Hola", "mundo")



"""Funcion para la suma de los parametros variables"""

def suma_numeros(*args):
    return sum(args)

print(suma_numeros(1, 2, 3))          # Salida: 6
print(suma_numeros(10, 20, 30, 40))  # Salida: 100










