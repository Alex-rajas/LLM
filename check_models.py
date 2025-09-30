import os
import requests
from dotenv import load_dotenv

# Cargar .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

headers = {"Authorization": f"Bearer {api_key}"}

# Hacer request a Groq para listar modelos
r = requests.get("https://api.groq.com/openai/v1/models", headers=headers)
print(r.json())
