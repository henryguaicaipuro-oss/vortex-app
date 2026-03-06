import streamlit as st
import pandas as pd

# Configuración
st.set_page_config(page_title="VORTEX INTELLIGENCE", layout="wide")

BASE_URL = "https://docs.google.com/spreadsheets/d/1eetJUNQ0pHAbHXJXJmy8mPxMYbMMdALoIbb7a8b5Suk"
GID_USUARIOS = "0" 
GID_PICKS = "1364408518" 

@st.cache_data(ttl=60)
def load_data(gid):
    url = f"{BASE_URL}/export?format=csv&gid={gid}"
    return pd.read_csv(url)

# Manejo de sesión corregido
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_data = None

if not st.session_state.logged_in:
    st.title("🔐 VORTEX LOGIN")
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    
    if st.button("ACCEDER"):
        df_users = load_data(GID_USUARIOS)
        # Búsqueda estricta
        user_row = df_users[(df_users['User'].astype(str) == user_input) & (df_users['Pass'].astype(str) == pass_input)]
        
        if not user_row.empty:
            st.session_state.logged_in = True
            st.session_state.user_data = user_row.iloc[0]
            st.rerun()
        else:
            st.error("Acceso incorrecto")
    st.stop()

# --- PANEL DE CONTROL ---
user = st.session_state.user_data
st.title(f"BIENVENIDO, {user['Name']}")
st.write(f"Tu plan actual: **{user['Plan']}**")

df_picks = load_data(GID_PICKS)
st.header("🎯 PICKS DEL DÍA")

for index, row in df_picks.iterrows():
    with st.container():
        st.markdown(f"### 🏀 {row['Juego']}")
        plan = str(user['Plan'])
        
        if plan == 'Básico':
            st.write(f"**Pick:** {row['Pick']}")
        elif plan == 'PRO':
            st.write(f"**Pick:** {row['Pick']}")
            st.write(f"**Análisis:** {row['Analisis_Tecnico']} | {row['Analisis_Narrativo']}")
        elif plan == 'VIP':
            st.write(f"**Pick:** {row['Pick']} (Prob: {row['Probabilidad']}%)")
            st.write(f"**Técnico:** {row['Analisis_Tecnico']}")
            st.write(f"**Narrativo:** {row['Analisis_Narrativo']}")
        st.markdown("---")
