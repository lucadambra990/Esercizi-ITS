#matchStatement esercizio Gemelli
n:int = int(input("Inserisci il numero di neonati: "))

match n:
    case 1:
        print("Congratulazioni!")
    case 2:
        print("Wow! Gemelli!!")
    case 3:
        print("Wow tre!")
    case 4:
        print("Mamma mia quattro! Wow!")
    case 5:
        print("Incredibile! Cinque!!")
    case _:
        print(f"Non ci credo! {n} bambini!!")