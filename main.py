from sfida_progr import SfidaProgrammazione
from sfida_ml import SfidaMachineLearning
from sfida_deep import SfidaDeepLearning

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
    
    # Variabile per il punteggio
    punteggio = 0

    # In base alla scelta, iniziamo la sfida corrispondente
    if scelta == "1":
        print("Hai scelto il percorso di Programmazione.")
        sfida = SfidaProgrammazione()
        punteggio = sfida.sfida_programmazione()
    
    elif scelta == "2":
        print("Hai scelto il percorso di Machine Learning.")
        sfida = SfidaMachineLearning()
        punteggio = sfida.sfida_machine_learning()
    
    elif scelta == "3":
        print("Hai scelto il percorso di Deep Learning.")
        sfida = SfidaDeepLearning()
        punteggio = sfida.sfida_deep_learning()
    
    else:
        print("Scelta non valida. Riavvia il programma e seleziona un'opzione valida.")
        return  # Terminiamo l'esecuzione

    # Dopo aver completato la sfida, gestiamo lo scontro finale se il punteggio è > 50
    if punteggio > 50:
        scontro = ScontroFinale()
        scontro.scontro_finale(punteggio)
    else:
        print(f"Il tuo punteggio finale è: {punteggio}.")
        print("Sei stato buttato fuori dall'aula da Tommaso")
    
if __name__ == "__main__":
    main()