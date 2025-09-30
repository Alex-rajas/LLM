import os
import requests
from dotenv import load_dotenv

# Cargar .env desde la raíz del proyecto
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(ROOT_DIR, ".env")
load_dotenv(dotenv_path=env_path)

# API Key de Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Modelos recomendados
DEFAULT_MODEL = "llama-3.1-8b-instant"
FALLBACK_MODELS = [
    "llama-3.3-70b-versatile",
    "gemma2-9b-it",
    "groq/compound",
    "groq/compound-mini"
]

def generate_text(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """
    Genera texto usando Groq API.
    
    Args:
        prompt (str): Texto o instrucción del usuario
        model (str): Modelo a utilizar (por defecto llama-3.1-8b-instant)
    
    Returns:
        str: Respuesta del modelo
    """
    if not GROQ_API_KEY:
        raise ValueError("❌ No se encontró GROQ_API_KEY en el archivo .env")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Eres un generador de contenido creativo para blogs y redes sociales."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 600
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except requests.exceptions.HTTPError as e:
        # Si el modelo no está disponible, probar modelos fallback
        if "model_decommissioned" in response.text.lower():
            for fallback in FALLBACK_MODELS:
                if fallback == model:
                    continue
                try:
                    return generate_text(prompt, model=fallback)
                except Exception:
                    continue
        # Si falla todo, lanzar el error original
        raise Exception(f"Error al generar contenido: {response.status_code} {response.text}")
    except Exception as e:
        raise Exception(f"Error en la petición a Groq: {e}")
