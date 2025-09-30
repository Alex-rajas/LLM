import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROK_API_KEY = os.getenv("GROK_API_KEY")

url = "https://api.x.ai/v1/models"

headers = {
    "Authorization": f"Bearer {GROK_API_KEY}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print("Response JSON:", response.json())
