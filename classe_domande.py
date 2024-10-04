class DomandeDataScience:
    def __init__(self):
        self.domande = []

    # Metodo per aggiungere una domanda al percorso
    def aggiungi_domanda(self, domanda, opzioni, risposta_corretta, punti_corretto, punti_errato):
        self.domande.append({
            "domanda": domanda,
            "opzioni": opzioni,
            "risposta_corretta": risposta_corretta,
            "punti_corretto": punti_corretto,
            "punti_errato": punti_errato
        })

    # Metodo per porre le domande e calcolare il punteggio
    def fai_domanda(self, numero_domanda):
        if numero_domanda >= len(self.domande):
            print("Numero di domanda non valido.")
            return 0

        domanda_data = self.domande[numero_domanda]
        print(domanda_data["domanda"])
        for i, opzione in enumerate(domanda_data["opzioni"]):
            print(f"{chr(65 + i)}: {opzione}")

        risposta = input("Inserisci la tua risposta (A, B, C, ecc.): ").upper()
        if risposta == domanda_data["risposta_corretta"]:
            print("Corretto!")
            return domanda_data["punti_corretto"]
        else:
            print(f"Sbagliato! La risposta corretta era {domanda_data['risposta_corretta']}.")
            return domanda_data["punti_errato"]

def percorso_programmazione():
    domande = DomandeDataScience()
    
    domande.aggiungi_domanda(
        "Quale funzione di Pandas permette di applicare una funzione a ogni riga o colonna di un DataFrame?",
        ["apply()", "map()", "groupby()"], 
        "A", 15, -10
    )
    
    domande.aggiungi_domanda(
        "Data una matrice NumPy, quale metodo usi per calcolare la somma cumulativa lungo un asse?",
        ["sum()", "cumsum()", "prod()"], 
        "B", 15, -10
    )
    
    domande.aggiungi_domanda(
        "In Pandas, come si elimina una colonna da un DataFrame senza modificarlo in modo permanente?",
        ["drop(inplace=False)", "drop(axis=1)", "remove(column)"], 
        "A", 15, -10
    )
    
    domande.aggiungi_domanda(
        "Cosa restituisce la funzione Python 'len()'?",
        ["Il tipo di un oggetto", "La dimensione di un file", "La lunghezza di una sequenza o collezione"], 
        "C", 15, -10
)
    
    domande.aggiungi_domanda(
        "In NumPy, cos'è il broadcasting?",
        ["Una tecnica per allineare array di forme diverse", "Un modo per suddividere gli array in blocchi", "Un metodo per sommare vettori"], 
        "A", 15, -10
    )
    
    punteggio = 0
    for i in range(5):
        punteggio += domande.fai_domanda(i)
    return punteggio
    