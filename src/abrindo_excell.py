import pandas as pd

#%% Abrir sheet especifica de um excel
 
df = pd.read_excel("../dados/exemplo.xlsx", "dados_1")

#%% Abrir arquivo e listar as sheets

arquivo_excel = pd.ExcelFile("../dados/exemplo.xlsx")

print(arquivo_excel.sheet_names)

df_aba1 = arquivo_excel.parse("dados_1")
df_aba2 = arquivo_excel.parse("dados_2")