import pandas as pd
import streamlit as st
import plotly_express as px

# Definindo o título da página
st.title("Trabalho do Sprint 5 - Análise do arquivo vehicles_us.csv")

# Lendo o arquivo veiculos.csv
car_data = pd.read_csv('vehicles_us.csv') # lendo os dados


# Subtítulo para a seção de histograma
st.subheader("Histograma")
# Exibindo os dados
hist_button = st.button('Criar histograma') # criar um botão   
if hist_button: # se o botão for clicado
     # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
     # criar um histograma
    fig = px.histogram(car_data, x="odometer")
     
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)



 # Subtítulo para a seção de histograma com caixa de seleção
st.subheader("Histograma - com caixa de seleção")

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    # Selecionar a coluna para o histograma
    column = st.selectbox('Selecione a coluna para o histograma', car_data.columns)
    st.write(f'Criando um histograma para a coluna {column}')
    
    # Criar o histograma para a coluna selecionada
    fig = px.histogram(car_data, x=column)
    st.plotly_chart(fig, use_container_width=True)



# Subtítulo para a seção de gráfico de dispersão
st.subheader("Gráfico de dispersão")
# Criar uma caixa de seleção para gráfico de dispersão
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter:
    # Selecionar as colunas para o gráfico de dispersão
    x_column = st.selectbox('Selecione a coluna para o eixo X', car_data.columns)
    y_column = st.selectbox('Selecione a coluna para o eixo Y', car_data.columns)
    st.write(f'Criando um gráfico de dispersão para {x_column} vs {y_column}')
    
    # Criar o gráfico de dispersão para as colunas selecionadas
    fig = px.scatter(car_data, x=x_column, y=y_column)
    st.plotly_chart(fig, use_container_width=True)