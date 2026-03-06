import streamlit as st
import pandas as pd

# Configuración de página profesional
st.set_page_config(page_title="VORTEX INTELLIGENCE", layout="wide")

# URL Base - Asegúrate de que el documento sea público
BASE_URL = "https://docs.google.com/spreadsheets/d/1eetJUNQ0pHAbHXJXJmy8mPxMYbMMdALoIbb7a8b5Suk"

# CSS para diseño oscuro elegante
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .card {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=60)
def get_sheet(sheet_name):
    url = f"{BASE_URL}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    return pd.read_csv(url)

# --- SISTEMA DE SESIÓN ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_data = None

if not st.session_state.logged_in:
    st.title("🔐 VORTEX INTELLIGENCE")
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    
    if st.button("ACCEDER"):
        try:
            df_users = get_sheet("USUARIOS")
            user_row = df_users[(df_users['User'].astype(str) == user_input) & 
                                (df_users['Pass'].astype(str) == pass_input)]
            
            if not user_row.empty:
                st.session_state.logged_in = True
                st.session_state.user_data = user_row.iloc[0]
                st.rerun()
            else:
                st.error("Acceso incorrecto. Verifica tus credenciales.")
        except Exception as e:
            st.error(f"Error crítico: {e}")
    st.stop()

# --- PANEL PRINCIPAL ---
user = st.session_state.user_data
st.title(f"🚀 VORTEX | Bienvenid@, {user['Name']}")
st.write(f"---")

try:
    df_picks = get_sheet("PICKS")
    
    # Filtrado inteligente
    for index, row in df_picks.iterrows():
        if row['Categoria_VIP'] == user['Plan'] or row['Categoria_VIP'] == 'Básico':
            with st.container():
                st.markdown(f"""
                <div class='card'>
                    <h3>🏀 {row['Juego']}</h3>
                    <p><b>Deporte:</b> {row['Deporte']} | <b>Mercado:</b> {row['Mercado']}</p>
                    <p><b>Pick:</b> {row['Pick']} | <b>Probabilidad:</b> {row['Probabilidad']}%</p>
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander("Ver Análisis Completo"):
                    st.write(f"**Edge:** {row['Valor_Edge']}")
                    st.write(f"**Técnico:** {row['Analisis_Tecnico']}")
                    st.write(f"**Narrativo:** {row['Analisis_Narrativo']}")
except Exception as e:
    st.error("No se pudieron cargar los picks. Por favor, verifica que la pestaña 'PICKS' exista.")

if st.button("Cerrar Sesión"):
    st.session_state.logged_in = False
    st.rerun()
