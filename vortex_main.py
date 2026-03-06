import streamlit as st
import pandas as pd

# Configuración inicial de la página
st.set_page_config(page_title="VORTEX INTELLIGENCE", layout="wide")

# Usamos la ID que ya configuraste en tus Secrets de Streamlit
SHEET_ID = st.secrets["SHEET_ID"]

# Función profesional para leer pestañas específicas mediante API de Google
@st.cache_data(ttl=60)
def get_data(sheet_name):
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    return pd.read_csv(url)

# CSS para diseño profesional oscuro
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0d1117 0%, #161b22 100%); color: white; }
    .card { background-color: #161b22; padding: 20px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 20px; }
    .header-text { color: #58a6ff; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- SISTEMA DE SESIÓN ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_data = None

if not st.session_state.logged_in:
    st.title("🔐 VORTEX INTELLIGENCE")
    user_input = st.text_input("Usuario")
    pass_input = st.text_input("Contraseña", type="password")
    
    if st.button("ACCEDER"):
        try:
            df_users = get_data("USUARIOS")
            user_row = df_users[(df_users['User'].astype(str) == user_input) & 
                                (df_users['Pass'].astype(str) == pass_input)]
            
            if not user_row.empty:
                st.session_state.logged_in = True
                st.session_state.user_data = user_row.iloc[0]
                st.rerun()
            else:
                st.error("Credenciales incorrectas")
        except Exception as e:
            st.error(f"Error de conexión: {e}")
    st.stop()

# --- PANEL PRINCIPAL (HOME) ---
user = st.session_state.user_data
st.title("📊 VORTEX DASHBOARD")
st.markdown(f"**Usuario:** {user['Name']} | **Plan:** {user['Plan']}")
st.write("---")

# Carga y filtrado de Picks
try:
    df_picks = get_data("PICKS")
    
    if df_picks.empty:
        st.warning("No hay picks disponibles en este momento.")
    else:
        for index, row in df_picks.iterrows():
            # Filtrado por categoría de usuario
            if row['Categoria_VIP'] == user['Plan'] or row['Categoria_VIP'] == 'Básico':
                with st.container():
                    st.markdown(f"""
                    <div class='card'>
                        <h3 class='header-text'>🏀 {row['Juego']}</h3>
                        <p><b>Mercado:</b> {row['Mercado']} | <b>Pick:</b> {row['Pick']}</p>
                        <p><b>Probabilidad:</b> {row['Probabilidad']}% | <b>Edge:</b> {row['Valor_Edge']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    with st.expander("🔍 Ver Análisis Completo"):
                        st.markdown("**Análisis Técnico (Sabermetría/Localía):**")
                        st.info(row['Analisis_Tecnico'])
                        st.markdown("**Análisis Narrativo (Real/Táctico):**")
                        st.success(row['Analisis_Narrativo'])
                        if 'Explicacion' in row and pd.notna(row['Explicacion']):
                            st.write(f"**Nota:** {row['Explicacion']}")

except Exception as e:
    st.error(f"Error cargando los picks: {e}")

if st.button("Cerrar Sesión"):
    st.session_state.logged_in = False
    st.rerun()
