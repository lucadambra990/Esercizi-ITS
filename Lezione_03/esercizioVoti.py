voto:int = int(input("Inserisci il tuo voto: "))

match voto:
    case 10:
        print("Eccellente!")
    case 8|9:
        print("Molto buono!")
    case 6|7:
        print("Sufficiente!")
    case 4|5:
        print("Insufficiente!")
    case 1|2|3:
        print("Gravemente insufficiente!")
    case _:
        print("Voto non valido!")

