"""
PROGETTO FINALE M1: Analisi di Vendite in una Catena di Negozi
Autore: Massimo Pelli
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Parte 1  Dataset di base
Creare un file CSV chiamato vendite.csv con almeno 30 righe che contenga le seguenti colonne:
Data (formato YYYY-MM-DD)
Negozio (stringa: es. Milano, Roma, Napoli)
Prodotto (stringa: es. Smartphone, Laptop, TV)
Quantità (intero)
Prezzo_unitario (float)

esempio riga:
2023-01-01, Milano, Smartphone, 5, 499.99
"""

print("=" * 60)
print("PARTE 1: Creazione del file vendite.csv")
print("=" * 60)

dati_vendite_grezzi = {
    "Data": [
        "2023-09-01", "2023-09-01", "2023-09-01", "2023-09-02", "2023-09-02", "2023-09-02",
        "2023-09-03", "2023-09-03", "2023-09-03", "2023-09-04", "2023-09-04", "2023-09-04",
        "2023-09-05", "2023-09-05", "2023-09-05", "2023-09-06", "2023-09-06", "2023-09-06",
        "2023-09-07", "2023-09-07", "2023-09-07", "2023-09-08", "2023-09-08", "2023-09-08",
        "2023-09-09", "2023-09-09", "2023-09-09", "2023-09-10", "2023-09-10", "2023-09-10",
        "2023-09-11", "2023-09-11", "2023-09-11", "2023-09-12", "2023-09-12", "2023-09-12"
    ],
    "Negozio": [
        "Milano", "Roma", "Napoli", "Milano", "Roma", "Torino",
        "Firenze", "Milano", "Roma", "Napoli", "Torino", "Milano",
        "Roma", "Firenze", "Napoli", "Milano", "Torino", "Roma",
        "Milano", "Napoli", "Firenze", "Roma", "Milano", "Torino",
        "Napoli", "Roma", "Milano", "Firenze", "Torino", "Roma",
        "Milano", "Napoli", "Roma", "Torino", "Firenze", "Milano"
    ],
    "Prodotto": [
        "Smartphone", "Laptop", "TV", "Tablet", "Smartwatch", "Smartphone",
        "Laptop", "TV", "Cuffie", "Smartphone", "Tablet", "Laptop",
        "TV", "Smartwatch", "Cuffie", "Smartphone", "Laptop", "TV",
        "Tablet", "Smartwatch", "Smartphone", "Laptop", "TV", "Cuffie",
        "Smartphone", "Tablet", "Laptop", "TV", "Smartwatch", "Cuffie",
        "Smartphone", "Laptop", "TV", "Tablet", "Smartwatch", "Cuffie"

    ],
    "Quantità": [
        5, 3, 2, 4, 8, 6,
        2, 3, 10, 4, 5, 2,
        3, 6, 12, 7, 3, 2,
        6, 5, 4, 3, 4, 15,
        5, 7, 4, 2, 8, 14,
        8, 2, 3, 5, 6, 11
    ],
    "Prezzo_unitario": [
        499.99, 899.99, 650.00, 299.99, 149.99, 499.99,
        899.99, 650.00, 79.99, 499.99, 299.99, 899.99,
        650.00, 149.99, 79.99, 499.99, 899.99, 650.00,
        299.99, 149.99, 499.99, 899.99, 650.00, 79.99,
        499.99, 299.99, 899.99, 650.00, 149.99, 79.99,
        499.99, 899.99, 650.00, 299.99, 149.99, 79.99
    ]
}

df_iniziale = pd.DataFrame(dati_vendite_grezzi)
df_iniziale.to_csv("vendite.csv", index=False)
print("File 'vendite.csv' creato con successo con", len(df_iniziale), "righe.")

"""
Parte 2 Importazione con Pandas
Importare il file CSV in un DataFrame Pandas e stampare:
le prime 5 righe (head())
il numero di righe e colonne (shape)
le informazioni generali (info())
"""
print("=" * 60)
print("PARTE 2: Importazione con Pandas")
print("=" * 60)

df = pd.read_csv("vendite.csv")
print("Prime 5 righe:")
print(df.head())
print("Numero di righe e colonne:", df.shape)
print("Informazioni generali:")
print(df.info())

"""
Parte 3 Elaborazioni con Pandas
Aggiungere una colonna Incasso calcolata come Quantità * Prezzo_unitario.
Calcolare con Pandas:
l’incasso totale di tutta la catena
l’incasso medio per negozio
i 3 prodotti più venduti (in termini di quantità totale)
Raggruppare i dati per Negozio e Prodotto e mostrare l’incasso medio.
"""

print("\n" + "=" * 60)
print("PARTE 3: Elaborazioni con Pandas")
print("=" * 60)

# Calcolo dell'incasso totale
df["Incasso"] = df["Quantità"] * df["Prezzo_unitario"]
incasso_totale = df["Incasso"].sum()
print("Incasso totale di tutta la catena:", incasso_totale)

#incasso medio per negozio
incasso_medio_negozio = df.groupby("Negozio")["Incasso"].mean()
print("\nIncasso medio per negozio:")
print(incasso_medio_negozio)

#top 3 prodotti più venduti in termini di quantità totale
top_3_prodotti = df.groupby("Prodotto")["Quantità"].sum().nlargest(3)
print("\nI 3 prodotti più venduti (in termini di quantità totale):")
print(top_3_prodotti)

# Raggruppamento dei dati per Negozio e Prodotto e calcolo dell'incasso medio
incasso_medio_gruppo = df.groupby(["Negozio", "Prodotto"])["Incasso"].mean()
print("\nIncasso medio per Negozio e Prodotto:")
print(incasso_medio_gruppo)

"""
Parte 4  Uso di NumPy
Estrarre la colonna Quantità come array NumPy e calcolare:
media, minimo, massimo e deviazione standard
percentuale di vendite sopra la media

Esempio parziale:
import numpy as np
q = df["Quantità"].to_numpy()
media = np.mean(q)
massimo = np.max(q)
Creare un array NumPy 2D che contenga solo Quantità e Prezzo_unitario e calcolare per ogni riga l’incasso. 
Confrontare i risultati con la colonna Incasso del DataFrame per verificarne la correttezza.
"""

print("\n" + "=" * 60)
print("PARTE 4: Elaborazioni numeriche e verifiche vettoriali con NumPy")
print("=" * 60)

# Estrazione della colonna Quantità come array NumPy
quantita_np = df["Quantità"].to_numpy()
media = np.mean(quantita_np)
minimo = np.min(quantita_np)
massimo = np.max(quantita_np)
deviazione_standard = np.std(quantita_np)
sopra_media = np.sum(quantita_np > media) / len(quantita_np) * 100

print("Media Quantità:", media)
print("Minimo Quantità:", minimo)
print("Massimo Quantità:", massimo)
print("Deviazione Standard Quantità:", deviazione_standard)
print("Percentuale di vendite sopra la media:", sopra_media, "%")

#Array 2D con Quantità e Prezzo_unitario
array_2d = df[["Quantità", "Prezzo_unitario"]].to_numpy()
incasso_np = array_2d[:, 0] * array_2d[:, 1]

#confronto con la colonna Incasso del DataFrame
if np.allclose(incasso_np, df["Incasso"].to_numpy()):
    print("Verifica: L'incasso calcolato con NumPy corrisponde alla colonna Incasso del DataFrame.")

"""
Parte 5 Visualizzazioni con Matplotlib
Creare i seguenti grafici:
Grafico a barre: incasso totale per ogni negozio
Grafico a torta: percentuale di incassi per ciascun prodotto
Grafico a linee: andamento giornaliero degli incassi totali della catena.

Esempio parziale (grafico a barre):
import matplotlib.pyplot as plt
df.groupby("Negozio")["Incasso"].sum().plot(kind="bar")
plt.show()
"""

print("\n" + "=" * 60)
print("PARTE 5: Generazione grafici con Matplotlib")
print("=" * 60)

# 1. Grafico a barre: Incasso totale per ogni negozio
incasso_per_negozio = df.groupby("Negozio")["Incasso"].sum()

plt.figure(figsize=(8, 5))
plt.bar(incasso_per_negozio.index, incasso_per_negozio.values, color="royalblue", edgecolor="black")
plt.title("Incasso Totale per Negozio", fontsize=13, fontweight="bold")
plt.xlabel("Negozio", fontsize=11)
plt.ylabel("Incasso Totale (€)", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()

# 2. Grafico a torta: Percentuale di incassi per ciascun prodotto
incasso_per_prodotto = df.groupby("Prodotto")["Incasso"].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    incasso_per_prodotto.values,
    labels=incasso_per_prodotto.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=plt.cm.Paired.colors
)
plt.title("Percentuale Incassi per Prodotto", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()

# 3. Grafico a linee: Andamento giornaliero degli incassi totali
incasso_giornaliero = df.groupby("Data")["Incasso"].sum()

plt.figure(figsize=(10, 5))
plt.plot(incasso_giornaliero.index, incasso_giornaliero.values, marker="o", color="darkgreen", linewidth=2)
plt.title("Andamento Giornaliero degli Incassi Totali della Catena", fontsize=13, fontweight="bold")
plt.xlabel("Data", fontsize=11)
plt.ylabel("Incasso Totale (€)", fontsize=11)
plt.xticks(rotation=45)
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()

"""
Parte 6 Analisi Avanzata
Creare una nuova colonna Categoria che raggruppi i prodotti in grandi famiglie (es. Smartphone e Laptop → Informatica, TV → Elettrodomestici)
Calcolare per ogni categoria:
incasso totale
quantità media venduta
Salvare il DataFrame aggiornato con le nuove colonne in un nuovo file vendite_analizzate.csv.
"""

print("\n" + "=" * 60)
print("PARTE 6: Analisi Avanzata per Categorie ed Esportazione")
print("=" * 60)

# Creazione della colonna Categoria
mappa_categorie = {
    "Smartphone": "Telefonia",
    "Smartwatch": "Telefonia",
    "Laptop": "Informatica",
    "Tablet": "Informatica",
    "TV": "Elettrodomestici",
    "Cuffie": "Audio"
}

df["Categoria"] = df["Prodotto"].map(mappa_categorie)

# Calcolo dell'incasso totale e quantità media venduta per categoria
report_categorie = df.groupby("Categoria").agg(
    incasso_totale=("Incasso", "sum"),
    quantita_media=("Quantità", "mean")
).round(2)

print("Report per Categoria:")
print(report_categorie)

# Salvataggio del DataFrame aggiornato in un nuovo file CSV
df.to_csv("vendite_analizzate.csv", index=False)
print("File 'vendite_analizzate.csv' creato con successo con le nuove colonne.")