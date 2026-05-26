import streamlit as st
import pandas as pd

# Título
st.title("Países Mais Seguros para Viajar")

# Ler arquivo CSV
df = pd.read_csv("paises.csv")

# Mostrar tabela
st.subheader("Tabela de Dados")
st.dataframe(df)

# Mostrar métricas
st.subheader("Informações")

st.write(f"Quantidade de países: {len(df)}")

# Filtro
pais = st.selectbox(
    "Escolha um país:",
    df["País /Região:"]
)

# Mostrar dados do país selecionado
resultado = df[df["País /Região:"] == pais]

st.write(resultado)
