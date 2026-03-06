import streamlit as st
import pandas as pd

# Configuración básica
st.set_page_config(page_title="VORTEX INTELLIGENCE", layout="wide")

# Función para cargar datos desde tu Google Sheet
def load_data(url):
    csv_url = url.replace('/edit#gid=', '/export?format=csv&gid=').replace('/edit?usp=sharing', '/export?format=csv')
    return pd.read_csv(csv_url)

# URL de tu Sheet (la que me pasaste)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1eetJUNQ0pHAbHXJXJmy8mPxMYbMMdALoIbb7a8b5Suk/edit?usp=sharing"

# Login simplificado
if 'user' not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    st.title("🔐 VORTEX LOGIN")
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    if st.button("ACCEDER"):
        df_users = load_data(SHEET_URL.replace("edit?usp=sharing", "edit#gid=0")) # Pestaña Usuarios
        user_row = df_users[(df_users['User'] == user_input) & (df_users['Pass'] == pass_input)]
        if not user_row.empty:
            st.session_state.user = user_row.iloc[0]
            st.rerun()
        else: st.error("Acceso incorrecto")
    st.stop()

# --- PANEL VIP/PRO/BASIC ---
user = st.session_state.user
st.title(f"BIENVENIDO, {user['Name']}")
st.write(f"Tu plan actual: **{user['Plan']}**")

df_picks = load_data(SHEET_URL.replace("edit?usp=sharing", "edit#gid=1364408518")) # Asegúrate de que este ID sea el de tu hoja PICKS

for index, row in df_picks.iterrows():
    # Lógica de visualización según Plan
    with st.container():
        st.subheader(f"🏀 {row['Juego']}")
        if user['Plan'] == 'Básico':
            st.write(f"Pick: {row['Pick']}")
        elif user['Plan'] == 'PRO':
            st.write(f"Pick: {row['Pick']}")
            st.write(f"Análisis: {row['Analisis_Tecnico']} | {row['Analisis_Narrativo']}")
        elif user['Plan'] == 'VIP':
            st.write(f"Pick: {row['Pick']} (Prob: {row['Probabilidad']}%)")
            st.write(f"Técnico: {row['Analisis_Tecnico']}")
            st.write(f"Narrativo: {row['Analisis_Narrativo']}")
