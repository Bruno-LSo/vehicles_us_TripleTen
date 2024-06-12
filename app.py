import pandas as pd
import streamlit as st
import plotly_express as px

# Definindo o título da página
st.title("Trabalho do Sprint 5 - Análise do arquivo veiculos.csv")

# Lendo o arquivo veiculos.csv
car_data = pd.read_csv('vehicles.csv') # lendo os dados

# Exibindo os dados
hist_button = st.button('Criar histograma') # criar um botão   
if hist_button: # se o botão for clicado
     # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
     # criar um histograma
    fig = px.histogram(car_data, x="odometer")
     
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    # Selecionar a coluna para o histograma
    column = st.selectbox('Selecione a coluna para o histograma', car_data.columns)
    st.write(f'Criando um histograma para a coluna {column}')
    
    # Criar o histograma para a coluna selecionada
    fig = px.histogram(car_data, x=column)
    st.plotly_chart(fig, use_container_width=True)