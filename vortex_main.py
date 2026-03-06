import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="VORTEX INTELLIGENCE", layout="wide")

# 2. CSS PARA EL LOOK TECNOLÓGICO (Fondo, Bordes, Menú)
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=1920');
        background-size: cover;
        background-attachment: fixed;
    }
    .main-container {
        background-color: rgba(13, 17, 23, 0.85);
        border: 1px solid #30363d;
        border-radius: 15px;
        padding: 30px;
        margin-top: 50px;
    }
    .nav-bar {
        display: flex;
        justify-content: space-around;
        background: rgba(22, 27, 34, 0.9);
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #58a6ff;
    }
    .nav-item { color: #ffffff; text-decoration: none; font-weight: bold; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

# 3. MENÚ SUPERIOR (Navegación)
st.markdown("""
    <div class='nav-bar'>
        <a class='nav-item' href='#'>[HOME]</a>
        <a class='nav-item' href='#'>[NOSOTROS]</a>
        <a class='nav-item' href='#'>[DEPORTES]</a>
        <a class='nav-item' href='#'>[EFECTIVIDAD]</a>
        <a class='nav-item' href='#'>[PLANES]</a>
        <a class='nav-item' href='#' style='color:#58a6ff;'>[SUSCRIPCIÓN]</a>
        <a class='nav-item' href='#'>[CONTACTO]</a>
    </div>
""", unsafe_allow_html=True)

# 4. LOGIN CENTRADO
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>🔐 VORTEX LOGIN</h1>", unsafe_allow_html=True)

user = st.text_input("Usuario")
pw = st.text_input("Contraseña", type="password")

if st.button("ACCEDER"):
    st.write("Conectando...")
    
st.markdown('</div>', unsafe_allow_html=True)
