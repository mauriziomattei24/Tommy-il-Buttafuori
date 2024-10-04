from classe_domande import percorso_programmazione #import di altre funzioni da mettere qua


def main():
    print("Benvenuto nel quiz di Data Science!")
    
    hr = input("Sei un HR? (y/n): ").lower()
    
    if hr == 'y':
        print("Mi dispiace, sei stato buttato fuori da Tommaso!")
        return  
    
    print("Seleziona un percorso:")
    print("1: Programmazione")
    print("2: Machine Learning")
    print("3: Deep Learning")
    
    scelta = input("Inserisci il numero corrispondente alla tua scelta: ")
    
    if scelta == "1":
        print("Hai scelto il percorso di Programmazione.")
        punteggio = percorso_programmazione()
        print(f"Il tuo punteggio finale è: {punteggio}")
    
    elif scelta == "2":
        print("Hai scelto il percorso di Machine Learning.")
        # punteggio = percorso_machine_learning()
        print(f"Il tuo punteggio finale è: {punteggio}")
    
    elif scelta == "3":
        print("Hai scelto il percorso di Deep Learning.")
        # punteggio = percorso_intelligenza_artificiale()
        print(f"Il tuo punteggio finale è: {punteggio}")
    
    else:
        print("Scelta non valida. Riavvia il programma e seleziona un'opzione valida.")
    
    if punteggio > 50:
        scontro_finale()
    else:
        print(f"Il tuo punteggio finale è: {punteggio}.")
        print("Sei stato buttato fuori dall'aula da Tommaso")
    
if __name__ == "__main__":
    main()




class ScontroFinale:
    def scontro_finale(self, punteggio):
        print(f"Sei arrivato allo scontro finale contro Tommaso con {punteggio} punti!")
        print("Preparati alla domanda finale...")

        # Chiede se piace SQL
        risposta_sql = input("Ti piace SQL? (si/no): ").strip().lower()

        if risposta_sql == "si":
            print("Hai sconfitto Tommaso! Hai vinto il gioco!")
        else:
            print("Tommaso ti ha buttato fuori dall'aula! Game over.")
