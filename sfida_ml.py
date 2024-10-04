from classe_domande import DomandeDataScience

class SfidaMachineLearning:
    def __init__(self):
        
        self.domande = DomandeDataScience()
        self.punteggio = 0  

    def aggiungi_domande(self):
        self.domande.aggiungi_domanda(
            "Qual è il principale obiettivo del machine learning supervisionato?",
            ["Identificare modelli nei dati non etichettati", 
             "Prevedere un risultato basato su dati etichettati", 
             "Ridurre il numero di variabili in un dataset"], 
            "B", 15, -10
        )
    
        self.domande.aggiungi_domanda(
            "Quale di queste metriche è comunemente utilizzata per valutare le prestazioni di un modello di classificazione?",
            ["Mean Square Error (MSE)", "R-Squared", "Accuracy"], 
            "C", 15, -10
        )
    
        self.domande.aggiungi_domanda(
            "Quale tra i seguenti algoritmi è un esempio di apprendimento non supervisionato?",
            ["Regressione Lineare", "K-Means Clustering", "Decision Tree"], 
            "B", 15, -10
        )
    
        self.domande.aggiungi_domanda(
            "Cosa rappresenta il termine 'overfitting' in un modello di machine learning?",
            ["Un modello che generalizza bene sui dati non visti", 
             "Un modello che si adatta troppo bene ai dati di addestramento, perdendo capacità di generalizzazione", 
             "Un modello che non ha sufficienti parametri per apprendere dai dati"], 
            "B", 15, -10
        )
    
        self.domande.aggiungi_domanda(
            "Qual è l'importanza della 'normalizzazione' nei dati di input?",
            ["Rimuovere i dati non necessari dal dataset", 
             "Garantire che tutte le variabili abbiano lo stesso intervallo per migliorare le prestazioni del modello", 
             "Aumentare la dimensione del dataset"], 
            "B", 15, -10
        )

    def sfida_machine_learning(self):
        
        self.aggiungi_domande()
        
       
        for i in range(5):
            self.punteggio += self.domande.fai_domanda(i)
        
        return self.punteggio  
