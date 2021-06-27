import pymssql
import pandas as pd

conn = pymssql.connect(
    server="ip-servidor",
    user="usuario",
    password="senha",
    database="banco"
)

def sql_table_to_pandas(table_name: str):
    cursor = conn.cursor(as_dict=True)
    cursor.execute(f'SELECT * FROM {table_name}')
    return pd.DataFrame(cursor.fetchall())