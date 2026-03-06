import streamlit as st
import pandas as pd

# Configuración básica
st.set_page_config(page_title="VORTEX", layout="centered")

# Lógica de carga
SHEET_ID = st.secrets["SHEET_ID"]

@st.cache_data(ttl=60)
def get_data(sheet_name):
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    return pd.read_csv(url)

# --- SISTEMA DE SESIÓN ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 VORTEX LOGIN")
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    if st.button("ACCEDER"):
        try:
            df = get_data("USUARIOS")
            user_row = df[(df['User'].astype(str) == user_input) & (df['Pass'].astype(str) == pass_input)]
            if not user_row.empty:
                st.session_state.logged_in = True
                st.session_state.user = user_row.iloc[0]
                st.rerun()
            else:
                st.error("Credenciales incorrectas")
        except Exception as e:
            st.error(f"Error: {e}")
    st.stop()

# --- PANEL PRINCIPAL (HOME) ---
user = st.session_state.user
st.title(f"🚀 BIENVENIDO, {user['Name']}")
st.write(f"Plan Activo: **{user['Plan']}**")

try:
    df_picks = get_data("PICKS")
    # Usamos contenedores nativos que ya vienen con diseño profesional
    for _, row in df_picks.iterrows():
        if row['Categoria_VIP'] == user['Plan'] or row['Categoria_VIP'] == 'Básico':
            with st.container(border=True):
                st.subheader(f"🏀 {row['Juego']}")
                st.write(f"**Pick:** {row['Pick']} | **Mercado:** {row['Mercado']}")
                
                # Análisis desplegable
                with st.expander("🔍 Ver Análisis"):
                    st.write("**Técnico:**")
                    st.info(row['Analisis_Tecnico'])
                    st.write("**Narrativo:**")
                    st.success(row['Analisis_Narrativo'])
except Exception:
    st.error("Error al cargar los datos.")

if st.button("Cerrar Sesión"):
    st.session_state.logged_in = False
    st.rerun()
