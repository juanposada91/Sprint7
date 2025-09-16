# Se importan las librerías necesarias

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Se lee el archivo CSV en un DataFrame

car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal de la apliación

st.header('Análisis de anuncios de venta de coches en Estados Unidos')

# Botón para construir histograma

hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Relación entre odómetro y precio')
    fig = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Odómetro vs Precio')
    st.plotly_chart(fig, use_container_width=True)
