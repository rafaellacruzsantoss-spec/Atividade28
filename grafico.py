import streamlit as st
import pandas as pd

# Título
st.title("Países Mais Seguros para Viajar")

# Ler CSV
df = pd.read_csv("paises.csv", sep=";")

# Mostrar dados
st.subheader("Tabela")
st.dataframe(df)

# Mostrar nomes das colunas
st.write(df.columns)

# Escolher colunas do gráfico
x = df.columns[0]
y = df.columns[1]

# Gráfico de barras
st.subheader("Gráfico")

st.bar_chart(
    data=df,
    x=x,
    y=y
)
