import streamlit as st

# URL de TU imagen de fondo (reemplázala por la tuya si tienes otra)
BG_IMAGE_URL = "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=1920"

st.set_page_config(page_title="VORTEX", layout="wide")

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{BG_IMAGE_URL}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    /* Capa oscura para que el texto resalte sobre la imagen */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.7);
        z-index: -1;
    }}
    /* Estilo para el recuadro central (donde irá el login) */
    .login-container {{
        background: rgba(13, 17, 23, 0.85);
        border: 1px solid #30363d;
        border-radius: 20px;
        padding: 50px;
        max-width: 500px;
        margin: auto;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# Contenido centrado
st.markdown('<div class="login-container">', unsafe_allow_html=True)
st.title("🔐 VORTEX LOGIN")
user = st.text_input("Usuario")
pw = st.text_input("Contraseña", type="password")
if st.button("ACCEDER"):
    st.write("Accediendo...")
st.markdown('</div>', unsafe_allow_html=True)
