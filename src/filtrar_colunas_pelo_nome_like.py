import pandas as pd

dict_dados = {"Medida a": [1, 2, 3],
              "Medida b": [4, 6, 3],
              "Result a": [4, 3, 1],
              "Result b": [1, 2, 3],
              "aaaaaaaa": [1, 1, 1],
              "a a a b": [2, 2, 2]}

df = pd.DataFrame(dict_dados)

"""Filter pode ser usado para filtrar linhas ou colunas contendo um
padrão de string, também é aceito regex"""

df_medidas = df.filter(like = "Medida")

#%% Usando regex

df_a = df.filter(regex = r"\ba$")

#%% Exemplo usando regex para produtar em um texto

import re

pattern = r'\ba$'
test_string = 'Medida a'
result = re.search(pattern, test_string)

print(result)

#%% Case insensitive

df_medida_insensitive = df.filter(regex = re.compile(r"medida", re.IGNORECASE))