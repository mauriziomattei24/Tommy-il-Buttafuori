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

    