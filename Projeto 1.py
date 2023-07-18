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

print(f'Dataset Shape : {df.shape}')
df.head()

df.info()

nans = df.isna().sum().sort_values(ascending = False)

pct = 100*nans/df.shape[0]
missing = pd.concat([nans, pct], axis = 1).rename({0 : 'Num of missing values', 1 : 'Percentage of missing values'}, axis = 1)

missing.head(20)

df[['prices.amountMin', 'prices.amountMax']].describe()

df = df[['brand', 'categories', 'dateAdded' , 'colors', 'name', 'imageURLs',
       'prices.amountMax', 'prices.color', 'prices.currency',]]

df.head()

df['brand'] = df['brand'].str.lower().str.strip().str.replace('@', 'a',  regex=True)


brands = ['aerosoles', 'kenneth cole', 'ellie', 'toms', 'ugg', 'pleaser', 'michael kors', 'ralph lauren',
          'puma', 'walking cradles', 'vionic', 'vince', 'victoria', 'valentino', 'adidas', 'bcbg', 'sperry',
          'spring step', 'nina' , 'moda'
         ]

for brand in  brands :
    filt = df['brand'].str.contains(brand).fillna(False)
    df.loc[filt, 'brand'] = brand

non_brands = ['famous name brand', 'generic', 'generic surplus', 'non-branded',
             'not applicable', 'not rated', 'lucky  brand', 'lucky brand', 'very fine dance shoes'
             ]
filt = df['brand'].isin(non_brands)
df.loc[filt, 'brand'] = 'unbranded'
df['brand'].fillna('unbranded', inplace = True)

ls = df['brand'].value_counts()[df['brand'].value_counts() < 20]
ls = list(ls.index)
filt = df['brand'].isin(ls)
df.loc[filt, 'brand'] = 'small brands'


df['brand'] = df['brand'].str.capitalize()

df['brand'].value_counts()





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

