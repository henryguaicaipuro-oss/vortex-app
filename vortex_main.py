import streamlit as st

# 1. Ajuste de configuración
st.set_page_config(page_title="VORTEX", layout="wide")

# 2. CSS simplificado (solo estilo de botones)
st.markdown("""
    <style>
    /* Forzar fondo oscuro */
    [data-testid="stAppViewContainer"] {
        background-color: #0d1117;
    }
    /* Estilo para los botones del menú */
    .stButton > button {
        background-color: transparent;
        color: white;
        border: 1px solid #30363d;
        width: 100%;
        border-radius: 5px;
    }
    .stButton > button:hover {
        border: 1px solid #58a6ff;
        color: #58a6ff;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Menú profesional usando Columnas (¡No falla!)
cols = st.columns([1, 1, 1, 1, 1, 1, 1])
botones = ["[HOME]", "[NOSOTROS]", "[DEPORTES]", "[EFECTIVIDAD]", "[PLANES]", "[SUSCRIPCIÓN]", "[CONTACTO]"]

for i, col in enumerate(cols):
    with col:
        st.button(botones[i])

st.markdown("---")
