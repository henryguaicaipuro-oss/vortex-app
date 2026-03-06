import streamlit as st
import pandas as pd

st.set_page_config(page_title="VORTEX", layout="wide")

SHEET_ID = st.secrets["SHEET_ID"]

@st.cache_data(ttl=60)
def get_data(sheet_name):
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    return pd.read_csv(url)

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

# --- PANEL PRINCIPAL ---
user = st.session_state.user
st.title(f"🚀 VORTEX | BIENVENIDO, {user['Name']}")
st.markdown("---")

try:
    df_picks = get_data("PICKS")
    # Filtramos para mostrar
    for _, row in df_picks.iterrows():
        if row['Categoria_VIP'] == user['Plan'] or row['Categoria_VIP'] == 'Básico':
            # Estructura de tarjeta con columnas para mejor legibilidad
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### 🏀 {row['Juego']}")
                st.write(f"**Pick:** {row['Pick']} | **Mercado:** {row['Mercado']}")
            with col2:
                st.metric("Probabilidad", f"{row['Probabilidad']}%")
            
            with st.expander("🔍 Ver Análisis Técnico y Narrativo"):
                st.markdown("**Técnico:**")
                st.info(row['Analisis_Tecnico'])
                st.markdown("**Narrativo:**")
                st.success(row['Analisis_Narrativo'])
            st.markdown("---") # Separador visual claro
except Exception:
    st.error("Error al cargar los datos. Verifica la pestaña 'PICKS'.")
