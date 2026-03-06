import streamlit as st
import pandas as pd

# Usamos la ID que ya configuraste en tus Secrets de Streamlit
SHEET_ID = st.secrets["SHEET_ID"]

# Función profesional para leer pestañas específicas
@st.cache_data(ttl=60)
def get_data(sheet_name):
    # Esta es la URL mágica que SÍ lee pestañas por nombre
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    return pd.read_csv(url)

st.set_page_config(page_title="VORTEX", layout="wide")

# --- LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 VORTEX LOGIN")
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    
    if st.button("ACCEDER"):
        try:
            df_users = get_data("USUARIOS")
            # Verificar credenciales
            user_row = df_users[(df_users['User'].astype(str) == user_input) & 
                                (df_users['Pass'].astype(str) == pass_input)]
            
            if not user_row.empty:
                st.session_state.logged_in = True
                st.session_state.user_data = user_row.iloc[0]
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos")
        except Exception as e:
            st.error(f"Error de conexión: {e}")
    st.stop()

# --- PANEL VIP ---
user = st.session_state.user_data
st.title(f"🚀 BIENVENIDO, {user['Name']}")
st.write(f"Tu plan actual: **{user['Plan']}**")

try:
    df_picks = get_data("PICKS")
    if not df_picks.empty:
        st.dataframe(df_picks, use_container_width=True)
    else:
        st.warning("No hay datos en la pestaña 'PICKS'.")
except Exception as e:
    st.error("No se pudo cargar la pestaña 'PICKS'. Verifica que el nombre sea exacto.")
