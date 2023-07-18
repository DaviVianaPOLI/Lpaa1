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

x=df2.nlargest(15,'prices.amountMax')
df2 = df.drop_duplicates(subset=['brand'])

plt.figure(figsize=(17, 8))
plt.barh(x['brand'],x['prices.amountMax'])
plt.xlabel('valor em dolar')
plt.title('Preço médio de sapatos para as 15 principais marcas')
plt.show()






