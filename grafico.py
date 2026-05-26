import streamlit as st
import pandas as pd

st.title("Países Mais Seguros")

# Ler CSV
df = pd.read_csv("paises.csv", sep=";", encoding="utf-8")

# Mostrar colunas
st.write("Colunas encontradas:")
st.write(df.columns)

# Mostrar tabela
st.dataframe(df)

# Escolher colunas
x = st.selectbox("Escolha coluna X", df.columns)
y = st.selectbox("Escolha coluna Y", df.columns)

# Criar gráfico
st.subheader("Gráfico de Barras")

st.bar_chart(
    data=df,
    x=x,
    y=y
)
