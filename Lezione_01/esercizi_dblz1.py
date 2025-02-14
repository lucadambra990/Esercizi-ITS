# import math
# # #Esercizio1
# # # print("Hello world")
# # a = float(input("Inserisci il valore dell'ipotenusa: "))
# # b = float(input("Inserisci il valore del cateto: "))
# # if a > b:
# #     c:float = math.sqrt((a**2)-(b**2))
# #     print(f"Il cateto C vale {c}")
# # else:
# #     print("Errore")


# # #Esercizio2
# # max:int = int(input("Inserisci il valore massimo per iniziare il confronto: "))
# # i = 1
# # while i < 4:
# #     n:int = int(input("Inserisci il numero: "))
# #     if n > max:
# #         max = n
# #     i +=1
# # print(f"Il valore massimo è {max}")


# # #Esercizio3
# # somma:int = 0
# # i = 1
# # while i<=5:
# #     n:int = int(input("Inserisci i numeri da sommare: "))
# #     if n > 0:
# #         somma += n
# #     i += 1
# # print(f"La somma tra i numeri inseriti è {somma}")


# # #Esercizio4
# # n:int = int(input("Inserisci un numero da verificare: "))
# # if n%2==0:
# #     print(f"il numero inserito {n} è pari")
# # else:
# #     print(f"il numero inserito {n} è dispari")


# #Esercizio5
# # primo: bool = True
# # n:int = int(input("inserire un numero da verificare: "))
# # if n < 2:
# #     print(f"Il numero inserito non è primo")
  
# # else:
# #     div = 2
# #     while div < n:
# #         if n % div == 0:
# #             print("Il numero non è primo")
# #             primo = False
# #             break
# #         div+=1


# # if primo:
# #     print("il numero è primo")


# #Esercizio6
# # n:int = int(input("Inserisci il numero di cui vuoi sapere il fattoriale: "))
# # if n > 0:
# #     fatt = 1
# #     i = 1
# #     while i<= n:
# #         fatt *= i
# #         i +=1
# #     print(f"il fattoriale di {n} è {fatt}")
# # else:
# #     print("Il numero deve essere positivo")


# #Esercizio7
# # pari:int = 0
# # dispari:int = 0
# # i = 0
# # while i<=10:
# #     n:int= int(input("Inserisci un numero: "))
# #     if n % 2 ==0:
# #         pari +=1
# #     else:
# #         dispari +=1
# #     i +=1
# # print(f"i numeri pari sono {pari}")
# # print(f"i numeri dispari sono {dispari}")


# #Esercizio8
# soglia:int = int(input("inserisci un valore soglia: "))
# i = 0
# while i <= 7:
#     n:int = int(input("Inserisci dei numeri: "))   
#     if n > soglia:
#         print(f"I numeri maggiori del valore soglia sono {n}")
#     i +=1


# #Esercizio9
# # nome:str = str(input("Inserire un nome di un venditore da confrontare: "))
# # vendite:int = int(input("Inserire un totale delle vendite da confrontare: "))
# # max_nome = nome
# # max = vendite
# # min_nome = nome
# # min = vendite
# # i = 0
# # while i <= 5:
# #     new_nome:str= str(input("Inserisci un nuovo nome da confrontare: "))
# #     new_vendite:int = int(input("Inserire un nuovo totale di vendite da confrontare: "))
# #     if new_vendite > max:
# #         max_nome = new_nome
# #         max = new_vendite
# #     elif new_vendite < min:
# #         min_nome = new_nome
# #         min = new_vendite
# #     i += 1
# # print(f"Il venditore {max_nome} ha il numero massimo di totale vendite: {max}")
# # print(f"Il venditore {min_nome} ha il numero minimo di totale vendite: {min}")


# #Esercizio10
# # redd:float = float(input("Inserisci il tuo reditto: "))
# # media:float = float(input("Inserisci la media dei voti: "))
# # if redd < 20000 and media > 27:
# #     print("Borsa di studio approvata")
# # else:
# #     print("Borsa di studio non approvata (Motivo: reddito o media insufficiente)")


# #Esercizio11
# posti_liberi:int = 20
# while True:
#     opzione:str = str(input("Inserire un opzione tra prenota - libera - visualizza - esci: "))
#     if opzione == "prenota":
#         if posti_liberi > 0:
#             posti_liberi -=1
#             print("Prenotazione effetuata con successo!")
#         else:
#             print("Non ci sono posti disponibili!")
#     elif opzione == "libera":
#         if posti_liberi < 20:
#             posti_liberi +=1
#             print("Posto di nuovo disponibile!")
#         else:
#             print("Tutti i posti sono già disponibili!")
#     elif opzione == "visualizza":
#         print(f"I posti liberi rimasti sono {posti_liberi}")
#         print(f"I posti occupati sono {20 - posti_liberi}")
#     elif opzione == "esci":
#         break
#     else:
#         print("Errore, inserisci un opzione tra ingresso - uscita - stato - esci")
