import os
import requests
import json
from dotenv import load_dotenv

# Cargar .env desde la raíz del proyecto
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(ROOT_DIR, ".env")
load_dotenv(dotenv_path=env_path)

def test_groq_api_direct():
    """Test directo de la API de Groq"""
    
    print("🔧 TEST DIRECTO DE API GROQ")
    print("=" * 50)
    
    # Obtener API key
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        print("❌ No se encontró GROQ_API_KEY en .env")
        return False
    
    print(f"✅ API Key encontrada: {api_key[:10]}...{api_key[-4:]}")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Test 1: Listar modelos disponibles
    print("\n🔍 Test 1: Verificando modelos disponibles")
    try:
        models_response = requests.get(
            "https://api.groq.com/openai/v1/models",
            headers=headers,
            timeout=10
        )
        
        print(f"Status modelos: {models_response.status_code}")
        if models_response.status_code == 200:
            models = models_response.json()
            available_models = [m["id"] for m in models.get("data", [])]
            print(f"✅ Modelos disponibles: {available_models}")
        else:
            print(f"❌ Error obteniendo modelos: {models_response.text}")
            return False
    except Exception as e:
        print(f"❌ Error en request de modelos: {e}")
        return False
    
    # Test 2: Hacer una petición simple
    test_models = ["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768"]
    
    for model in test_models:
        print(f"\n🧪 Test 2: Probando modelo {model}")
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": "Responde solo con 'Test exitoso'"}],
            "max_tokens": 10,
            "temperature": 0.1
        }
        
        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                result = response.json()
                message = result["choices"][0]["message"]["content"]
                print(f"✅ Respuesta exitosa: {message}")
                return True
            else:
                print(f"❌ Error {response.status_code}: {response.text}")
        except Exception as e:
            print(f"❌ Excepción: {e}")
    
    return False

def test_api_key_format():
    """Verificar formato de la API key"""
    print("\n🔑 VERIFICACIÓN DE API KEY")
    print("-" * 30)
    
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ API key no encontrada")
        return False
    
    print(f"Longitud: {len(api_key)} caracteres")
    print(f"Primeros 10: {api_key[:10]}")
    print(f"Últimos 4: {api_key[-4:]}")
    
    if api_key.startswith("gsk_"):
        print("✅ Formato parece correcto (empieza con gsk_)")
    else:
        print("⚠️  Formato inusual (no empieza con gsk_)")
    
    return True

if __name__ == "__main__":
    print("🚀 DIAGNÓSTICO COMPLETO DE GROQ API")
    print("=" * 60)
    
    test_api_key_format()
    success = test_groq_api_direct()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 ¡API de Groq funciona correctamente!")
    else:
        print("❌ API de Groq aún no responde bien")
        print("👉 Revisa que la API key sea válida y tengas acceso en https://console.groq.com")
