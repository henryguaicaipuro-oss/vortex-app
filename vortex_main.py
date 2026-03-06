import streamlit as st
import pandas as pd

# Configuración de diseño
st.set_page_config(page_title="VORTEX INTELLIGENCE", layout="wide")

# Configuración de IDs (ASEGÚRATE DE QUE SEAN LOS CORRECTOS)
BASE_URL = "https://docs.google.com/spreadsheets/d/1eetJUNQ0pHAbHXJXJmy8mPxMYbMMdALoIbb7a8b5Suk"
GID_USUARIOS = "0" 
GID_PICKS = "1364408518" # <-- VERIFICA ESTE NÚMERO EN TU NAVEGADOR

# Función para cargar datos
@st.cache_data(ttl=60) # Actualiza cada 60 segundos
def load_data(gid):
    url = f"{BASE_URL}/export?format=csv&gid={gid}"
    return pd.read_csv(url)

# Login
if 'user' not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    st.title("🔐 VORTEX LOGIN")
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    
    if st.button("ACCEDER"):
        df_users = load_data(GID_USUARIOS)
        # Filtramos buscando coincidencia exacta
        user_row = df_users[(df_users['User'].astype(str) == user_input) & (df_users['Pass'].astype(str) == pass_input)]
        
        if not user_row.empty:
            st.session_state.user = user_row.iloc[0]
            st.rerun()
        else:
            st.error("Acceso incorrecto o usuario no registrado")
    st.stop()

# --- PANEL DE CONTROL ---
user = st.session_state.user
st.title(f"BIENVENIDO, {user['Name']}")
st.write(f"Tu plan actual: **{user['Plan']}**")

# Carga de Picks
df_picks = load_data(GID_PICKS)

# Mostrar tabla de picks según el Plan
st.header("🎯 PICKS DEL DÍA")

for index, row in df_picks.iterrows():
    with st.container():
        st.markdown(f"### 🏀 {row['Juego']}")
        
        # Lógica de niveles
        if user['Plan'] == 'Básico':
            st.write(f"**Pick:** {row['Pick']}")
            
        elif user['Plan'] == 'PRO':
            st.write(f"**Pick:** {row['Pick']}")
            st.write(f"**Análisis Técnico:** {row['Analisis_Tecnico']}")
            st.write(f"**Análisis Narrativo:** {row['Analisis_Narrativo']}")
            
        elif user['Plan'] == 'VIP':
            st.write(f"**Pick:** {row['Pick']}")
            st.write(f"**Probabilidad:** {row['Probabilidad']}%")
            st.write(f"**Análisis Técnico:** {row['Analisis_Tecnico']}")
            st.write(f"**Análisis Narrativo:** {row['Analisis_Narrativo']}")
            st.write(f"**Explicación:** {row['Explicacion']}")
        
        st.markdown("---")
