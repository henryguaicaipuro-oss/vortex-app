import streamlit as st

# Configuración de página
st.set_page_config(page_title="VORTEX INTELLIGENCE", layout="wide")

# CSS para el Fondo estilo "Dashboard Tech" y contenedor principal
st.markdown("""
    <style>
    /* Fondo oscuro con degradado profesional */
    .stApp {
        background: radial-gradient(circle at center, #1b2631 0%, #0d1117 100%);
        color: #e6edf3;
    }
    
    /* Contenedor central con borde neón sutil */
    .main-box {
        background-color: rgba(22, 27, 34, 0.8);
        border: 1px solid #30363d;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Estructura del Layout
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("🔐 VORTEX LOGIN")
st.write("Bienvenido al sistema de inteligencia deportiva.")

# Espacio para los inputs (aquí irán los botones en el siguiente paso)
user = st.text_input("Usuario")
pw = st.text_input("Contraseña", type="password")
if st.button("ACCEDER"):
    st.write("Autenticando...")

st.markdown('</div>', unsafe_allow_html=True)
