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
    
if __name__ == "__main__":
    main()
