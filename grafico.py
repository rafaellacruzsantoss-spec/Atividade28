import streamlit as st
import pandas as pd
df = pd.read_csv('
display(df.head())
df.to_csv('dados_exportados.csv', index=False)
print('DataFrame exportado com sucesso para dados_exportados.csv')
