from classe_domande import DomandeDataScience


class SfidaMachineLearning:
    def __init__(self):
        self.domande = DomandeDataScience()
        self.punteggio = 0
    
    def aggiungi_domande(self):
        # Aggiunge le domande predefinite
        self.domande.aggiungi_domanda(
        domanda = "Qual è il principale obiettivo del machine learning supervisionato?",
        opzioni = "A) Identificare modelli nei dati non etichettati. \nB) Prevedere un risultato basato su dati etichettati. \nC) Ridurre il numero di variabili in un dataset.",
        risposta_corretta = "A",
        punti_corretto = 15,
        punti_errato = -10
    )

        self.domande.aggiungi_domanda(
        domanda = "Quale di queste metriche è comunemente utilizzata per valutare le prestazioni di un modello di classificazione?",
        opzioni = "A) Mean Square Error (MSE) \nB) R-Squared \nC) Accuracy",
        risposta_corretta = "C",
        punti_corretto = 15,
        punti_errato = -10
    )

        self.domande.aggiungidomanda(
        domanda="Quale tra i seguenti algoritmi è un esempio di apprendimento non supervisionato?",
        opzioni = "A) Regressione Lineare \nB) K-Means Clustering \nC) Decision Tree",
        risposta_corretta = "B",
        punti_corretto = 15,
        punti_errato = -10
    )

        self.domande.aggiungidomanda(
        domanda="Cosa rappresenta il termine 'overfitting' in un modello di machine learning?",
        opzioni = "A) Un modello che generalizza bene sui dati non visti. \nB) Un modello che si adatta troppo bene ai dati di addestramento, perdendo capacità di generalizzazione. \nC)  Un modello che non ha sufficienti parametri per apprendere dai dati.",
        risposta_corretta = "B",
        punti_corretto = 15,
        punti_errato = -10
    )

        self.domande.aggiungidomanda(
        domanda= "Qual è l'importanza della 'normalizzazione' nei dati di input?",
        opzioni = "A) Rimuovere i dati non necessari dal dataset. \nB) Garantire che tutte le variabili abbiano lo stesso intervallo per migliorare le prestazioni del modello. \nC) Aumentare la dimensione del dataset.",
        risposta_corretta = "B",
        punti_corretto = 15,
        punti_errato = -10
    )
    
    def sfida_machine_learning(self):
        # Fa tre domande e calcola il punteggio
        for i in range(5):
            self.punteggio += self.domande.fai_domanda(i)
        return self.punteggio