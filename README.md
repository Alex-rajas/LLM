# 📝 Generador de Contenido — Digital Content PoC

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.25-orange)
![Groq API](https://img.shields.io/badge/Groq-API-red)

## Descripción

Este proyecto es una **prueba de concepto (PoC)** para un sistema de generación automática de contenido textual utilizando **inteligencia artificial generativa**.  

Permite crear contenido adaptado a varias plataformas y audiencias:

- 🖋 Blogs  
- 🐦 Twitter/X  
- 📸 Instagram  
- 💼 LinkedIn  

Se ha desarrollado usando **Groq API** para la generación de texto y **Streamlit** para la interfaz web.

---

## 🚀 Características

- Generación de contenido para múltiples plataformas y audiencias.  
- Inputs personalizables: `tema`, `audiencia`, `plataforma`, `tono`.  
- Manejo de errores y fallback automático a modelos activos de Groq.  
- Extensible: se puede integrar generación de imágenes, RAG, agentes o publicación automática.  

---

## 🛠 Tecnologías

- **Python 3.10+**  
- **Streamlit**: interfaz web  
- **LangChain**: manejo de prompts  
- **Requests**: comunicación con la API de Groq  
- **dotenv**: gestión de variables de entorno  

---

## 📁 Estructura del proyecto

LLM/

├─ app.py # Interfaz web principal

├─ services/

│ ├─ init.py # Paquete Python

│ └─ groq_client.py # Cliente para Groq API

├─ .env # Variables de entorno (API Key)

├─ requirements.txt # Dependencias

└─ venv/ # Entorno virtual


---

## ⚙️ Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/Alex-rajas/LLM
cd LLM

```
2. Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate

```





