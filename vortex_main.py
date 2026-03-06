import streamlit as st
import pandas as pd

st.set_page_config(page_title="VORTEX INTELLIGENCE", layout="wide")

# URL directa a la hoja publicada (CSV)
# Asegúrate de usar la URL que obtuviste en la última imagen
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS4RGwfxroSVTSUY6bER9XtTjdyYAVnz_Uevir114_cRY33jW4aELS7Ob_8Jv6z-e5BtGRCpz5alL/pub?output=csv"

@st.cache_data(ttl=60)
def load_all_data():
    return pd.read_csv(CSV_URL)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_data = None

if not st.session_state.logged_in:
    st.title("🔐 VORTEX LOGIN")
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    
    if st.button("ACCEDER"):
        df_all = load_all_data()
        # Filtramos solo la parte de usuarios (asumiendo que los usuarios están arriba)
        # Si esto falla, intenta usando: df_users = df_all.iloc[:10]
        user_row = df_all[(df_all['User'].astype(str) == user_input) & (df_all['Pass'].astype(str) == pass_input)]
        
        if not user_row.empty:
            st.session_state.logged_in = True
            st.session_state.user_data = user_row.iloc[0]
            st.rerun()
        else:
            st.error("Acceso incorrecto")
    st.stop()

# --- PANEL DE CONTROL ---
st.title(f"BIENVENIDO, {st.session_state.user_data['Name']}")
df_picks = load_all_data()

st.header("🎯 PICKS DEL DÍA")
# Mostramos la tabla completa para verificar la carga
st.dataframe(df_picks)
