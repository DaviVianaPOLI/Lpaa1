"""
Projeto 1 de LPAA - Análise e Exploração de Dados 
Women's Shoes Prices Analysis

@author: DaviVianaPOLI


"""
#Importando as bibliotecas que serão utilizadas no projeto
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Carregando o arquivo dataset
df = pd.read_csv(r'C:\Users\daviv\OneDrive\Área de Trabalho\pyton\archive\Datafiniti_Womens_Shoes.csv')

top_brands = list(df['brand'].value_counts().head(30).index)
top_30 = df[df['brand'].isin(top_brands)]

mean_price = top_30.groupby('brand')[['prices']].mean().sort_values(by = 'prices', ascending = False)
mean_price = mean_price.reset_index()

mean_price.head()

x=df2.nlargest(15,'prices.amountMax')
df2 = df.drop_duplicates(subset=['brand'])





df.columns

plt.figure(figsize=(17, 8))
plt.barh(df['brand'],df['prices.amountMax'])
plt.xlabel('Ocorrência de Fatalidades')
plt.title('valor/dolar')
plt.show()

df[['prices.amountMin', 'prices.amountMax']].describe()

df = df[['brand', 'categories', 'dateAdded' , 'colors', 'name', 'imageURLs',
       'prices.amountMax', 'prices.color', 'prices.currency']]

df.head()

