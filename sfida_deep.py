from classe_domande import DomandeDataScience

class SfidaDeepLearning:
    def __init__(self):
        self.domande = DomandeDataScience()
        self.punteggio = 0
        self.aggiungi_domande()
    
    def aggiungi_domande(self):
        # Aggiunge le domande predefinite
        self.domande.aggiungi_domanda("Cos’è l'overfitting?", 
                                      ["A) Un problema di fitting del tuo modello sui dati", 
                                       "B) Quando il modello ha imparato i dati a memoria e si crede un genio", 
                                       "C) Un buon modo per passare le notti insonni cercando di risolverlo."], 
                                      "B", 15, -10)
        
        self.domande.aggiungi_domanda("Cos’è il dropout?", 
                                      ["A) Una tecnica per far perdere ogni speranza al modello", 
                                       "B) Quando il modello ha deciso che alcuni neuroni meritano una vacanza", 
                                       "C) Il momento in cui tu stesso vuoi lasciare il deep learning"], 
                                      "B", 15, -10)
        
        self.domande.aggiungi_domanda("Perché i miei risultati peggiorano quando aggiungo più layer?", 
                                      ["A) Perché il modello si distrae e inizia a filosofare sull’universo.", 
                                       "B) Perché ogni layer in più è un altro problema da risolvere", 
                                       "C) Perché hai raggiunto la profondità di confusione del modello"], 
                                      "C", 15, -10)
        
        self.domande.aggiungi_domanda("Cosa significa batch size?", 
                                      ["A) La dimensione della squadra di dati che fai passare tutti insieme", 
                                       "B) Il numero di neuroni che riesci a contare prima di addormentarti", 
                                       "C) La quantità di caffè che consumi per fare il tuning dei parametri"], 
                                      "A", 15, -10)
        
        self.domande.aggiungi_domanda("Cos'è una funzione di attivazione?", 
                                      ["A) Il pulsante magico che accende il cervello del modello", 
                                       "B) Quando il modello è così sveglio che non dorme più", 
                                       "C) Un modo complicato per rendere il modello nervoso con la matematica"], 
                                      "A", 15, -10)
    
    def sfida_deep_learning(self):
        # Fa tre domande e calcola il punteggio
        self.aggiungi_domande()
        self.punteggio = 0
        for i in range(5):
            self.punteggio += self.domande.fai_domanda(i)
        return self.punteggio
