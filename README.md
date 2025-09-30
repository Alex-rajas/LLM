📝 Generador de Contenido — Digital Content PoC
Descripción

Este proyecto es una prueba de concepto (PoC) de un sistema de generación automática de contenido para diversas plataformas utilizando inteligencia artificial generativa.

Permite crear contenido de texto adaptado a:

Blogs

Twitter/X

Instagram

LinkedIn

Se ha implementado utilizando Groq API y Streamlit, con prompts dinámicos que adaptan el contenido según la audiencia, plataforma y tono deseado.

🔹 Características

Generación de contenido para múltiples plataformas y audiencias.

Inputs personalizables: tema, audiencia, plataforma, tono.

Manejo de errores y fallback automático a modelos activos de Groq.

Estructura modular y extensible para integrar más funcionalidades (imágenes, RAG, publicación automática).

🛠️ Tecnologías

Python 3.10+

Streamlit: interfaz web

LangChain: manejo de prompts

Requests: comunicación con la API de Groq

dotenv: gestión de variables de entorno

📁 Estructura del proyecto
LLM/
├─ app.py                     # Interfaz web principal
├─ services/
│   ├─ __init__.py            # Paquete Python
│   └─ groq_client.py         # Cliente para Groq API
├─ .env                       # Variables de entorno (API Key)
├─ requirements.txt            # Dependencias
└─ venv/                      # Entorno virtual

⚙️ Instalación

Clonar el repositorio:

git clone <url-del-repositorio>
cd LLM


Crear e activar entorno virtual:

python -m venv venv
venv\Scripts\activate      # Windows
# o
source venv/bin/activate   # Linux/Mac


Instalar dependencias:

pip install -r requirements.txt


Configurar .env con tu API Key de Groq:

GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxx

🚀 Uso

Ejecutar la aplicación Streamlit:

streamlit run app.py


Luego, en la interfaz web:

Introduce el tema y audiencia.

Selecciona la plataforma y el tono.

Haz clic en Generar contenido.

Obtendrás el texto listo para publicar.

⚡ Modelos usados

Por defecto: llama-3.1-8b-instant

Fallbacks: llama-3.3-70b-versatile, gemma2-9b-it, groq/compound, groq/compound-mini

Si algún modelo deja de estar disponible, el cliente Groq intentará automáticamente los modelos alternativos.

📝 Notas

Esta PoC está enfocada en minimizar coste, usando modelos disponibles con pruebas gratuitas o locales.

Es extensible: se puede agregar generación de imágenes, RAG para contenido más informado, agentes y publicación automática en redes.

📌 Licencia

MIT License — puedes usarlo y modificarlo para tu PoC sin restricciones.