import streamlit as st
import pandas as pd

# Configuración básica
st.set_page_config(page_title="VORTEX", layout="wide")

# CSS simplificado y directo
st.markdown("""
    <style>
    .stApp { background-color: #0e1117 !important; color: white !important; }
    div[data-testid="stVerticalBlock"] > div:nth-child(n) { border: 1px solid #333; padding: 15px; border-radius: 10px; margin-bottom: 10px; background-color: #1c1f26; }
    </style>
""", unsafe_allow_html=True)

# Lógica de carga (igual a la anterior)
SHEET_ID = st.secrets["SHEET_ID"]

@st.cache_data(ttl=60)
def get_data(sheet_name):
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    return pd.read_csv(url)

# --- PANEL DE CONTROL ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    user = st.text_input("Usuario")
    pw = st.text_input("Clave", type="password")
    if st.button("ACCEDER"):
        df = get_data("USUARIOS")
        if not df[(df['User'].astype(str) == user) & (df['Pass'].astype(str) == pw)].empty:
            st.session_state.logged_in = True
            st.session_state.user = df[(df['User'].astype(str) == user)].iloc[0]
            st.rerun()
else:
    st.title(f"Bienvenido, {st.session_state.user['Name']}")
    df_picks = get_data("PICKS")
    for _, row in df_picks.iterrows():
        st.subheader(f"🏀 {row['Juego']}")
        st.write(f"**Pick:** {row['Pick']} | **Mercado:** {row['Mercado']}")
        with st.expander("Análisis"):
            st.write(row['Analisis_Tecnico'])
