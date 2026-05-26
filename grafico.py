import streamlit as st
import pandas as pd

df = pd.read_csv('/content/sample_data/Paisescsv')
display(df.head())
df.to_csv('dados_exportados.csv', index=False)
print('DataFrame exportado com sucesso para dados_exportados.csv')
