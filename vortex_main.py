import streamlit as st
import pandas as pd

st.set_page_config(page_title="VORTEX INTELLIGENCE", layout="wide")

BASE_URL = "https://docs.google.com/spreadsheets/d/1eetJUNQ0pHAbHXJXJmy8mPxMYbMMdALoIbb7a8b5Suk"
GID_USUARIOS = "0" 
GID_PICKS = "1364408518" 

@st.cache_data(ttl=60)
def load_data(gid):
    url = f"{BASE_URL}/export?format=csv&gid={gid}"
    return pd.read_csv(url)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_data = None

if not st.session_state.logged_in:
    st.title("🔐 VORTEX LOGIN")
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    if st.button("ACCEDER"):
        df_users = load_data(GID_USUARIOS)
        user_row = df_users[(df_users['User'].astype(str) == user_input) & (df_users['Pass'].astype(str) == pass_input)]
        if not user_row.empty:
            st.session_state.logged_in = True
            st.session_state.user_data = user_row.iloc[0]
            st.rerun()
        else: st.error("Acceso incorrecto")
    st.stop()

# Panel VIP
user = st.session_state.user_data
st.title(f"BIENVENIDO, {user['Name']}")
df_picks = load_data(GID_PICKS)

st.header("🎯 PICKS DEL DÍA")
for index, row in df_picks.iterrows():
    # Solo mostrar si coincide con el nivel o si es abierto
    if row['Categoria_VIP'] == user['Plan'] or row['Categoria_VIP'] == 'Básico':
        with st.container():
            st.markdown(f"### 🏀 {row['Juego']} - {row['Deporte']}")
            st.write(f"**Mercado:** {row['Mercado']} | **Pick:** {row['Pick']}")
            st.write(f"**Probabilidad:** {row['Probabilidad']}% | **Valor:** {row['Valor_Edge']}")
            st.write(f"**Análisis Técnico:** {row['Analisis_Tecnico']}")
            st.write(f"**Análisis Narrativo:** {row['Analisis_Narrativo']}")
            st.markdown("---")
