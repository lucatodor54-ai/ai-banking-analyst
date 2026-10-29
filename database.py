import sqlite3
import pandas as pd

def creeaza_baza_de_date():
    df = pd.read_csv("banking_data.csv")

    conexiune = sqlite3.connect("banking.db")

    df.to_sql(
        "tranzactii",
        conexiune,
        if_exists="replace",
        index=False
    )
    conexiune.close()

def executa_query(query):
    conexiune = sqlite3.connect("banking.db")
    rezultat = pd.read_sql_query(query, conexiune)
    conexiune.close()
    return rezultat

query = """
SELECT nume, SUM(suma) AS total_tranzactii
FROM tranzactii
GROUP BY nume
ORDER BY total_tranzactii DESC;
"""

print(executa_query(query))