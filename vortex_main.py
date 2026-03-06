import streamlit as st
import pandas as pd

# Configuración
st.set_page_config(page_title="VORTEX INTELLIGENCE", layout="wide")

# ESTA ES LA URL DE TU PUBLICACIÓN (La que aparece en la cajita de la última imagen)
BASE_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS4RGwfxroSVTSUY6bER9XtTjdyYAVnz_Uevir114_cRY33jW4aELS7Ob_8Jv6z-e5BtGRCpz5alL/pub?output=csv"

@st.cache_data(ttl=60)
def load_data():
    # Al publicar todo el documento, los datos están en el CSV principal
    return pd.read_csv(BASE_URL)

# Manejo de sesión
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_data = None

if not st.session_state.logged_in:
    st.title("🔐 VORTEX LOGIN")
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    
    if st.button("ACCEDER"):
        # Cargamos los datos
        df_all = load_data()
        
        # Como publicaste todo el documento, necesitamos separar las hojas.
        # Streamlit lee el CSV como una sola tabla. 
        # Asegúrate de que en tu hoja de Google, la pestaña "USUARIOS" sea la primera.
        df_users = df_all # Aquí ajustaremos según cómo se vea la carga
        
        user_row = df_users[(df_users['User'].astype(str) == user_input) & (df_users['Pass'].astype(str) == pass_input)]
        
        if not user_row.empty:
            st.session_state.logged_in = True
            st.session_state.user_data = user_row.iloc[0]
            st.rerun()
        else:
            st.error("Acceso incorrecto")
    st.stop()

# --- PANEL DE CONTROL ---
st.title(f"BIENVENIDO, {st.session_state.user_data['Name']}")
st.write("Cargando picks...")
# ... (resto de tu lógica de visualización)
