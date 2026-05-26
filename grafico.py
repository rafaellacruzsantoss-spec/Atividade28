import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
fig, ax = plt.subplots(figsize=(12, 6))
df['Indícies:'] = df['Indícies:'].str.replace(',', '.', regex=False).astype(float)

# Sort the DataFrame by 'Indícies:' for better visualization
df_sorted = df.sort_values(by='Indícies:', ascending=False)

# Create a bar plot
df_sorted.plot(kind='bar', x='País /Região:', y='Indícies:', ax = ax , title='Indíces por País/Região')
plt.xlabel('País /Região:')
plt.ylabel('Indícies:')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.gca().spines[['top','right']].set_visible(False)
plt.tight_layout() # Adjust layout to prevent labels from overlapping
st.pyplot(fig)
