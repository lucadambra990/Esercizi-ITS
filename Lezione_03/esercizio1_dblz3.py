#Esercizio1
posti_max:int = int(input("Inserisci il numero di posti massimi del parcheggio: "))
posti_liberi = posti_max
while True:
    opz:str = str(input("Inserisci un opzione: "))
    if opz == "ingresso":
        if posti_liberi > 0:
            posti_liberi -= 1
            print("è stato effettuato un ingresso")
        else:
            print("Il parcheggio è pieno!")
    elif opz == "uscita":
        if posti_liberi < posti_max:
            posti_liberi += 1
            print("Si è liberato un posto nel parcheggio")
        else:
            print("Il parcheggio è già vuoto")
    elif opz == "stato":
        print(f"I posti liberi sono {posti_liberi}")
        print(f"I posti occupati sono {posti_max - posti_liberi}")
    elif opz == "esci":
        break
    else:
        print("Errore, inserisci un opzione tra ingresso - uscita - stato - esci")


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
