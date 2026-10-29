import os
import re
from dotenv import load_dotenv
from openai import OpenAI
from database import executa_query

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def genereaza_sql(intrebare):
    prompt = f"""
Esti un Data Analyst specializat in SQL si banking.

Ai o baza de date SQLite cu tabelul:

tranzactii(
    transaction_id INTEGER,
    client_id INTEGER,
    nume TEXT,
    oras TEXT,
    tip_tranzactie TEXT,
    suma REAL,
    data TEXT
)

Transforma intrebarea utilizatorului intr-un query SQL SQLite.

REGULI:
- Genereaza DOAR SELECT.
- Nu folosi INSERT, UPDATE, DELETE, DROP sau ALTER.
- Foloseste doar tabelul tranzactii.
- Returneaza doar query-ul SQL, fara explicatii si fara ```.

Intrebare:
{intrebare}
"""

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    return response.output_text.strip()


def query_sigur(query):
    query_curat = query.strip().lower()

    if not query_curat.startswith("select"):
        return False

    comenzi_interzise = [
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "create",
        "replace"
    ]

    for comanda in comenzi_interzise:
        if re.search(rf"\b{comanda}\b", query_curat):
            return False

    return True


def raspunde_la_intrebare(intrebare, df=None):

    query = genereaza_sql(intrebare)

    print("\nSQL generat de AI:")
    print(query)

    if not query_sigur(query):
        return "Query-ul generat nu este permis."

    try:
        rezultat = executa_query(query)
    except Exception as eroare:
        return f"Eroare SQL: {eroare}"

    if rezultat.empty:
        return "Nu am gasit rezultate pentru aceasta intrebare."

    prompt_final = f"""
Esti un Data Analyst bancar.

Utilizatorul a intrebat:
{intrebare}

Query-ul SQL executat a fost:
{query}

Rezultatul obtinut din baza de date este:
{rezultat.to_string(index=False)}

Explica rezultatul clar, scurt si profesional in limba romana.
Nu inventa informatii.
"""

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt_final
    )

    return response.output_text