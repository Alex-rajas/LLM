import streamlit as st
from langchain.prompts import PromptTemplate
from services.groq_client import generate_text

# Título de la app
st.set_page_config(page_title="Generador de Contenido — Digital Content PoC")
st.title("📝 Generador de Contenido — Digital Content PoC")

# Templates de prompts por plataforma
templates = {
    "blog": """Escribe un artículo para un blog sobre {tema}.
Audiencia: {audiencia}.
Estilo: {tono}.
Longitud: 3 párrafos.""",

    "twitter": """Escribe 3 tweets sobre {tema}.
Audiencia: {audiencia}.
Estilo: {tono}.
Cada tweet máximo 280 caracteres.""",

    "instagram": """Escribe un caption de Instagram sobre {tema}.
Audiencia: {audiencia}.
Estilo: {tono}.
Incluye emojis y hashtags.""",

    "linkedin": """Escribe un post profesional para LinkedIn sobre {tema}.
Audiencia: {audiencia}.
Estilo: {tono}.
Longitud: 100-200 palabras."""
}

# Inputs del usuario
tema = st.text_input("Tema", "")
audiencia = st.text_input("Audiencia", "")
plataforma = st.selectbox("Plataforma", ["blog", "twitter", "instagram", "linkedin"])
tono = st.selectbox("Tono", ["neutral", "informal", "profesional", "divulgativo", "infantil"])

# Botón de generación
if st.button("Generar contenido"):

    if not tema or not audiencia:
        st.warning("Por favor, completa el tema y la audiencia.")
    else:
        # Crear prompt
        prompt_template = PromptTemplate(
            input_variables=["tema", "audiencia", "tono"],
            template=templates[plataforma]
        )
        final_prompt = prompt_template.format(tema=tema, audiencia=audiencia, tono=tono)

        # Generar contenido con Groq
        try:
            with st.spinner("Generando contenido... ⏳"):
                content = generate_text(final_prompt)
            st.subheader("Contenido generado:")
            st.write(content)
        except Exception as e:
            st.error(f"❌ Error al generar contenido: {e}")

