#Chiedi all'utente di inserire il giorno e il mese
giorno:int = int(input("Inserisci il giorno: "))
mese:int = int(input("Inserisci il mese: "))

#Definisci la tupla con la data
data = (giorno, mese)

day_for_mese:list[int] = [31,29,31,30,31,30,31,31,30,31,30,31]

#Utilizzo del match statement per verificare la festività
match data:
    case(giorno,mese) if giorno <=0 or mese<=0:
        print("Inserire un valore positivo per il giorno e per il mese")
    case(1,1):
        print("Il 1/1 è Capodanno!")
    case(14,2):
        print("Il 14/2 è San Valentino")
    case(2,6):
        print("Il 2/6 è la Festa della Repubblica Italiana")
    case(15,8):
        print("il 15/8 è Ferragosto")
    case(31,10):
        print("Il 31/10 è Halloween")
    case(25,12):
        print("Il 25/12 è Natale")
    case(giorno, mese) if mese > 12 or giorno > day_for_mese[mese-1]:
        (f"Il {giorno}/{mese} non esiste!")
    case _:
        print("Nessuna festività importante in questa data")