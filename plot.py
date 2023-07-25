import matplotlib.pyplot as plt
import seaborn as sns

class PLT:
    def barra(x,title,xlabel,ylabel):
        plt.figure(figsize=(12, 6))
        x.plot(kind='bar', color='skyblue')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    def boxplot(x,y,title,xlabel,ylabel):
        plt.figure(figsize=(12, 6))
        plt.boxplot(x, labels=y, vert=False)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.tight_layout()
        plt.show()

    def hist(x,title,xlabel,ylabel):
        plt.figure(figsize=(10, 6))
        plt.hist(x, bins=30, color='skyblue', edgecolor='black')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
