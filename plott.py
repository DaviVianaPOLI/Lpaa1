# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 20:47:28 2023

@author: Acer
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Plott: 
    def barcolor(g, xlabel, ylabel, title):
        plt.figure(figsize=(12, 8), dpi=250)

       



        
        coluna1 = g.iloc[:, 0]

        # Define um esquema de cores mais agradável
        colors = plt.cm.tab20(range(len(g.index)))

        # Cria o gráfico de barras horizontais
        plt.barh(g.index, coluna1, color=colors)

        # Adiciona rótulos dentro das barras
        #for i, v in enumerate(g.values):
         #   plt.text(v + 0.2, i, str(v), color='black', va='center')

        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.title(title, fontsize=14)

        plt.xticks(rotation=45, ha='right')

        plt.show()