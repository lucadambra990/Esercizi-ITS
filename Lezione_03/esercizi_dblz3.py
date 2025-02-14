#Esercizio1
# posti_max:int = int(input("Inserisci il numero di posti massimi del parcheggio: "))
# posti_liberi = posti_max
# while True:
#     opz:str = str(input("Inserisci un opzione: "))
#     if opz == "ingresso":
#         if posti_liberi > 0:
#             posti_liberi -= 1
#             print("è stato effettuato un ingresso")
#         else:
#             print("Il parcheggio è pieno!")
#     elif opz == "uscita":
#         if posti_liberi < posti_max:
#             posti_liberi += 1
#             print("Si è liberato un posto nel parcheggio")
#         else:
#             print("Il parcheggio è già vuoto")
#     elif opz == "stato":
#         print(f"I posti liberi sono {posti_liberi}")
#         print(f"I posti occupati sono {posti_max - posti_liberi}")
#     elif opz == "esci":
#         break
#     else:
#         print("Errore, inserisci un opzione tra ingresso - uscita - stato - esci")


#Esercizio1 con condizione while diversa
# posti_max:int = int(input("Inserisci il numero di posti massimi del parcheggio: "))
# posti_liberi = posti_max
# opzione: str = None
# while opzione != "esci":
#     opzione: str = str(input("Scegliere un opzione tra ingresso - uscita - stato - esci: "))
#     if opzione == "ingresso":
#         if posti_liberi > 0:
#             posti_liberi -= 1
#             print("è stato effettuato un ingresso")
#         else:
#             print("Il parcheggio è pieno!")
#     elif opzione == "uscita":
#         if posti_liberi < posti_max:
#             posti_liberi += 1
#             print("Si è liberato un posto nel parcheggio")
#         else:
#             print("Il parcheggio è già vuoto")
      
#     elif opzione == "stato":
#         print(f"I posti liberi sono {posti_liberi}")
#         print(f"I posti occupati sono {posti_max - posti_liberi}")
#     elif opzione == "esci":
#         pass
#     else:
#         print("Errore inserire un opzione tra  ingresso - uscita - stato - esci")




#Esercizio2
# macchine_NS:int = int(input("Inserisci il numero di macchine provenienti dalla tratta nord/sud: "))
# macchine_EO:int = int(input("Inserisci il numero di macchine provenienti dalla tratta est/ovest: "))
# soglia:int = int(input("Inserire il valore soglia per ogni tratta: "))
# tempo_prio:int = int(input("Inserire il tempo prioritario delle tratte: "))
# if macchine_NS > soglia:
#     if macchine_EO > soglia:
#         tempo_NS = 50
#         tempo_EO = 50
#     else:
#         tempo_NS = tempo_prio
#         tempo_EO = 100- tempo_prio
# else:
#     if macchine_NS > soglia:
#         tempo_NS = 100 - tempo_prio
#         tempo_EO = tempo_prio       
#     else:
#         veicoli_tot = macchine_EO + macchine_NS
#         tempo_NS:float = (macchine_NS/veicoli_tot)*100
#         tempo_EO:float = 100 - tempo_NS
# print(f"Il tempo per la tratta nord/sud è {tempo_NS:.2f}%")
# print(f"Il tempo per la tratta est/ovest è {tempo_EO:.2f}%")


#Esercizio3
#Gestione corsi divisa in parte amministrativa e pubblica
corsi:dict = {
  
}
ruolo:str = input("Inserisci il tuo ruolo: ")
if ruolo == "amministratore":
    
   while True:


       ingresso = input("Cosa vuoi fare?")


       if ingresso == "Inserisci":


           nome_corso: str = input("Inserisci nome del corso: ")
          
           posti_massimi: int = int(input("Inserisci il numero massimo di alunni per corso: "))
           posti_disponibili: int = posti_massimi


           corsi[nome_corso] = {"posti_massimi": posti_massimi, "posti_disponibili": posti_disponibili}
      
       elif ingresso == "Esci":
               break
       elif ingresso == "Visualizza":
               print(corsi)


elif ruolo != "ammistratore":
   opzione:str = input("Inserisci un opzione tra -iscrizione -annulla -visualizza -esci")
   corso: str = input("A quale corso vuoi iscriverti?")
   if corso not in corsi:
       print("Errore, il corso...")
  
   elif opzione == "iscrizione":


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




   elif opzione == "Esci":
        pass
   else:
       print("Errore, inserire un opzione tra quelle elencate!!!")