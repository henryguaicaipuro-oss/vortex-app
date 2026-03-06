import streamlit as st

# Configuración inicial
st.set_page_config(page_title="VORTEX", layout="wide")

# CSS para la barra de navegación tipo "Menú de Diseño"
st.markdown("""
    <style>
    /* Resetear márgenes para que el menú pegue arriba */
    .block-container { padding-top: 2rem; }
    
    .nav-bar-vortex {
        display: flex;
        justify-content: center;
        gap: 30px;
        padding: 20px;
        background: rgba(0, 0, 0, 0.4);
        border-bottom: 1px solid rgba(88, 166, 255, 0.3);
        margin-bottom: 50px;
    }
    
    .nav-link {
        color: #8b949e;
        font-family: 'Arial', sans-serif;
        font-size: 14px;
        text-decoration: none;
        letter-spacing: 1px;
    }
    
    .nav-link:hover, .nav-link.active {
        color: #58a6ff;
    }
    </style>

    <div class="nav-bar-vortex">
        <a class="nav-link active" href="#">[HOME]</a>
        <a class="nav-link" href="#">[NOSOTROS]</a>
        <a class="nav-link" href="#">[DEPORTES]</a>
        <a class="nav-link" href="#">[EFECTIVIDAD]</a>
        <a class="nav-link" href="#">[PLANES]</a>
        <a class="nav-link" href="#" style="color: #58a6ff; border: 1px solid #58a6ff; padding: 2px 10px;">[SUSCRIPCIÓN]</a>
        <a class="nav-link" href="#">[CONTACTO]</a>
    </div>
""", unsafe_allow_html=True)
