import streamlit as st
import pandas as pd

st.set_page_config(page_title="VORTEX INTELLIGENCE", layout="wide")

# URL base
BASE_URL = "https://docs.google.com/spreadsheets/d/1eetJUNQ0pHAbHXJXJmy8mPxMYbMMdALoIbb7a8b5Suk"

# CSS para login y contenedores
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .card { background-color: #1c1f26; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=60)
def get_sheet(sheet_name):
    url = f"{BASE_URL}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    return pd.read_csv(url)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 VORTEX LOGIN")
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    
    if st.button("ACCEDER"):
        df_users = get_sheet("USUARIOS")
        user_row = df_users[(df_users['User'].astype(str) == user_input) & 
                            (df_users['Pass'].astype(str) == pass_input)]
        
        if not user_row.empty:
            st.session_state.logged_in = True
            st.session_state.user_data = user_row.iloc[0]
            st.rerun()
        else:
            st.error("Credenciales incorrectas")
    st.stop()

# --- PANEL PRINCIPAL ---
user = st.session_state.user_data
st.title(f"🚀 BIENVENIDO, {user['Name']}")

df_picks = get_sheet("PICKS")

if df_picks.empty:
    st.warning("No hay picks disponibles en este momento. Revisa tu hoja de cálculo.")
else:
    for _, row in df_picks.iterrows():
        # Verificación básica por si falta la columna Categoria_VIP
        categoria = row['Categoria_VIP'] if 'Categoria_VIP' in row else 'Básico'
        
        if categoria == user['Plan'] or categoria == 'Básico':
            with st.container():
                st.markdown(f"""
                <div class='card'>
                    <h3>🏀 {row['Juego']}</h3>
                    <p><b>Pick:</b> {row['Pick']} | <b>Prob:</b> {row['Probabilidad']}%</p>
                </div>
                """, unsafe_allow_html=True)
                with st.expander("Ver Análisis"):
                    st.write(f"**Técnico:** {row['Analisis_Tecnico']}")
                    st.write(f"**Narrativo:** {row['Analisis_Narrativo']}")

if st.button("Cerrar Sesión"):
    st.session_state.logged_in = False
    st.rerun()
