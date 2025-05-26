import streamlit as st
import pandas as pd
import plotly.express as px

# Carga de datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de Vehículos Usados 🚗')

# Casilla de verificación para histograma
show_hist = st.checkbox('Mostrar Histograma de Odómetro')
if show_hist:
    st.write('Distribución del kilometraje de los vehículos.')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
show_scatter = st.checkbox('Mostrar Gráfico de Dispersión: Odómetro vs Precio')
if show_scatter:
    st.write('Relación entre el kilometraje y el precio.')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)
