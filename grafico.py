import streamlit as st
import pandas as pd

st.title("Tabela de Países")

# Ler arquivo
df = pd.read_csv("Paises.csv", sep=";")

# Mostrar tabela
st.dataframe(df)

# Informações
st.write(df.shape)
