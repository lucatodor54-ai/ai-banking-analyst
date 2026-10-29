import pandas as pd


def incarca_date(nume_fisier):
    df = pd.read_csv(nume_fisier)
    return df


def suma_totala_tranzactii(df):
    return df["suma"].sum()


def valoare_medie_tranzactii(df):
    return df["suma"].mean()


def tranzactie_maxima(df):
    index_maxim = df["suma"].idxmax()
    return df.loc[index_maxim]


def total_pe_client(df):
    return df.groupby("nume")["suma"].sum().sort_values(ascending=False)


def total_pe_oras(df):
    return df.groupby("oras")["suma"].sum().sort_values(ascending=False)


def total_pe_tip_tranzactie(df):
    return df.groupby("tip_tranzactie")["suma"].sum().sort_values(ascending=False)


def numar_tranzactii_pe_client(df):
    return df["nume"].value_counts()


def top_client(df):
    totaluri = df.groupby("nume")["suma"].sum()
    client = totaluri.idxmax()
    valoare = totaluri.max()

    return client, valoare


def tranzactii_mari(df, prag=5000):
    return df[df["suma"] > prag]


def statistici_generale(df):
    return df["suma"].describe()