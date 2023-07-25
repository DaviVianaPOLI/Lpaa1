"""
Projeto 1 de LPAA - Análise e Exploração de Dados 
Women's Shoes Prices Analysis

@author: DaviVianaPOLI


"""
#Importando as bibliotecas que serão utilizadas no projeto
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from plot import PLT

#Carregando o arquivo dataset
df = pd.read_csv(r'C:\Users\Acer\Documents\pyton\lpaa1\Datafiniti_Womens_Shoes.csv')

###########################################################################################

#Top 10 marcas

# Selecionar colunas relevantes
df = df[['brand', 'prices.amountMax']]

# Remover linhas com preços ausentes (NaN)
df = df.dropna(subset=['prices.amountMax'])

# Calcular o preço médio de cada marca
average_prices_by_brand = df.groupby('brand')['prices.amountMax'].mean()

# Selecionar as top 10 marcas com base no preço médio
top_10_brands = average_prices_by_brand.nlargest(10)

# Plotar o gráfico de barras
PLT.barra(top_10_brands,"Top 10 Marcas de Sapatos Femininos por Preço Médio","Marca","Preço Médio")

###########################################################################################

#Contagem de sapato por marca
PLT.barra(df['brand'].value_counts().nlargest(10),'Top 10 Marcas com Mais Sapatos Femininos','Marca','Quantidade')

###########################################################################################

#Um boxplot permite ver a distribuição dos preços de sapatos por marca e ajuda a identificar possíveis outliers
PLT.boxplot([df[df['brand'] == brand]['prices.amountMax'] for brand in top_10_brands.index],top_10_brands.index,'Boxplot de Preços por Marca (Top 10)','Preço','Marca')

###########################################################################################

#Um histograma para visualizar a distribuição dos preços dos sapatos no dataset.
PLT.hist(df['prices.amountMax'],'Histograma de Preços de Sapatos Femininos','Preço','Frequência')


PLT.distrib(df)






