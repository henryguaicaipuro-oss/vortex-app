import streamlit as st
import pandas as pd

# Usamos el formato de exportación directa que Google Sheets permite para archivos públicos
BASE_URL = "https://docs.google.com/spreadsheets/d/1eetJUNQ0pHAbHXJXJmy8mPxMYbMMdALoIbb7a8b5Suk"

@st.cache_data(ttl=60)
def get_sheet(sheet_name):
    # Esta URL descarga la pestaña específica como CSV
    url = f"{BASE_URL}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    return pd.read_csv(url)

st.title("🔐 VORTEX INTELLIGENCE")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
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
                st.error("Acceso incorrecto")
        except Exception as e:
            st.error(f"Error de conexión con Sheets: {e}")
    st.stop()

# --- PANEL VIP ---
user = st.session_state.user_data
st.write(f"Bienvenido, {user['Name']}")
df_picks = get_sheet("PICKS")
st.dataframe(df_picks)
