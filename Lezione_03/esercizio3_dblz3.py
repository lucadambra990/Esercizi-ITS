#Esercizio3
#Gestione corsi divisa in parte amministrativa e pubblica
corsi:dict = {
  
}
while True:
    ruolo:str = input("Inserisci il tuo ruolo oppure esci: ")
    if ruolo == "amministratore":
    
        while True:


            ingresso = input("Cosa vuoi fare? ")


            if ingresso == "Inserisci":


                nome_corso: str = input("Inserisci nome del corso: ")
                
                posti_massimi: int = int(input("Inserisci il numero massimo di alunni per corso: "))
                posti_disponibili: int = posti_massimi


                corsi[nome_corso] = {"posti_massimi": posti_massimi, "posti_disponibili": posti_disponibili}
            
            elif ingresso == "Esci":
                    break
            elif ingresso == "Visualizza":
                    print(corsi)


    elif ruolo == "studente":
        while True:
            opzione:str = input("Inserisci un opzione tra -iscrizione -annulla -visualizza -esci: ")
            
            if opzione == "Esci":
                    break
            corso: str = input("A quale corso sei interessato?: ")
            if corso not in corsi:
                print("Errore, il corso...")
            
            if opzione == "iscrizione":
                

                if corsi[corso]["posti_disponibili"] > 0:
                    corsi[corso]["posti_disponibili"] -= 1
                else:
                    print("Per questo corso non ci sono posti disponibili!")
            
            elif opzione == "annulla":
                if corsi[corso]["posti_disponibili"] != corsi[corso]["posti_massimi"]:
                        corsi[corso]["posti_disponibili"] += 1
                
                else:
                        print("Il corso è vuoto!")
            elif opzione == "visualizza":
                print(corsi[corso], corsi[corso]["posti_massimi"])
                print(corsi[corso], corsi[corso]["posti_disponibili"])

            else:
                print("Errore, inserire un opzione tra quelle elencate!!!")
                
    elif ruolo =="esci":
        break

#creare funzioni per stampare dizionario