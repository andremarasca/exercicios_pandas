# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html
# https://stackoverflow.com/questions/46405373/odbc-sql-type-155-is-not-yet-supported/46415933#46415933

import pyodbc
import pandas as pd

def retornar_conexao_sql():
    server = "DESKTOP-15TQLGD\SQLEXPRESS"
    database = "AdventureWorks2016"
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao

#Retornando a conexão SQL
conn = retornar_conexao_sql()


# Comando SQL
sql = "SELECT TOP 10 * FROM Person.Address"


dados = pd.read_sql(sql, conn)

dados.head(10)