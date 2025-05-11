# Importar librerias 
import streamlit as st
import pandas as pd
import plotly.express as px
# Cargar datos
df = pd.read_csv('vehicles_us.csv')
# Título de la app
st.title('Análisis de datos de vehículos')
# Casilla de verificación para histograma
if st.checkbox('Mostrar histograma de odómetro'):
    st.write('Histograma del odómetro (kilometraje)')
    fig_hist = px.histogram(df, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión de odómetro vs precio'):
    st.write('Dispersión entre odómetro y precio')
    fig_scatter = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)
