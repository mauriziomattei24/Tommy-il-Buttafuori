from classe_domande import DomandeDataScience

class SfidaProgrammazione:
    def __init__(self):
        # Inizializziamo una istanza della classe DomandeDataScience
        self.domande = DomandeDataScience()

    def aggiungi_domande(self):
        self.domande.aggiungi_domanda(
            "Quale funzione di Pandas permette di applicare una funzione a ogni riga o colonna di un DataFrame?",
            ["apply()", "map()", "groupby()"], 
            "A", 15, -10
        )
    
        self.domande.aggiungi_domanda(
            "Data una matrice NumPy, quale metodo usi per calcolare la somma cumulativa lungo un asse?",
            ["sum()", "cumsum()", "prod()"], 
            "B", 15, -10
        )
    
        self.domande.aggiungi_domanda(
            "In Pandas, come si elimina una colonna da un DataFrame senza modificarlo in modo permanente?",
            ["drop(inplace=False)", "drop(axis=1)", "remove(column)"], 
            "A", 15, -10
        )
    
        self.domande.aggiungi_domanda(
            "Cosa restituisce la funzione Python 'len()'?",
            ["Il tipo di un oggetto", "La dimensione di un file", "La lunghezza di una sequenza o collezione"], 
            "C", 15, -10
        )
    
        self.domande.aggiungi_domanda(
            "In NumPy, cos'è il broadcasting?",
            ["Una tecnica per allineare array di forme diverse", "Un modo per suddividere gli array in blocchi", "Un metodo per sommare vettori"], 
            "A", 15, -10
        )

    def sfida_programmazione(self):
       
        self.aggiungi_domande()
        self.punteggio = 0
        for i in range(5):
            self.punteggio += self.domande.fai_domanda(i)
        
        return self.punteggio 