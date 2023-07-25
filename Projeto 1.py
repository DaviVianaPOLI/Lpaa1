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

##########  Organizando pra colocar o gráfico  ##########

df2 = df.drop_duplicates(subset=['brand'])
df2=df2.nlargest(15,'prices.amountMax')

# Inverte a ordem das marcas no eixo y
marcas = df2['brand'][::-1]
valores = df2['prices.amountMax'][::-1]

combined_df = pd.DataFrame({'coluna1': marcas, 'coluna2': valores})

combined_df = combined_df.set_index(combined_df.columns[0])

combined_df[combined_df.columns[0]] = pd.to_numeric(combined_df[combined_df.columns[0]], errors='coerce')

Plott.barcolor(df2, 'Valor em dólar', 'Marcas', 'Preço médio de sapatos para as 15 principais marcas')


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

'''
plt.figure(figsize=(12, 8), dpi=250)

# Define um esquema de cores mais agradável
colors = plt.cm.tab20(range(len(marcas)))

# Cria o gráfico de barras horizontais
plt.barh(marcas, valores, color=colors)

# Adiciona rótulos dentro das barras
for i, v in enumerate(valores):
    plt.text(v + 0.2, i, str(v), color='black', va='center')

plt.xlabel('Valor em dólar', fontsize=12)
plt.ylabel('Marcas', fontsize=12)
plt.title('Preço médio de sapatos para as 15 principais marcas', fontsize=14)

plt.show()

'''





