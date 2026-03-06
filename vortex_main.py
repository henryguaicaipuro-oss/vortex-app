import streamlit as st
import pandas as pd

# 1. Cargamos datos
df = pd.read_csv("https://docs.google.com/spreadsheets/d/TU_ID/gviz/tq?tqx=out:csv&sheet=PICKS")

# 2. Layout simple (sin CSS complejo)
st.set_page_config(layout="wide")

# Barra lateral para navegación (Botones nativos)
nav = st.sidebar.radio("MENÚ VORTEX", ["HOME", "DEPORTES", "EFECTIVIDAD"])

if nav == "HOME":
    st.title("BIENVENIDO AL DASHBOARD")
    st.metric("Total Picks", len(df))
elif nav == "DEPORTES":
    st.title("ANÁLISIS DEPORTIVO")
    st.dataframe(df)

# Esto es 100% gratuito, se publica en 1 clic y es profesional
