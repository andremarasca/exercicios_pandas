import pandas as pd

#%% Abrir sheet especifica de um excel
 
df = pd.read_excel("../dados/exemplo.xlsx", "dados_1")


# É possível ordenar por vários níveis e escolher a ordem de cada nível.

df2 = df.sort_values(by=["Coluna 1", "Coluna 2"], ascending=[False, True])