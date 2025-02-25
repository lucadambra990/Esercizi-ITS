#esercizio nome e gender in input
nome:str = input("Inserisci il tuo nome: ")
gender:str = input("inserisci il tuo gender (m or f): ")

match gender:
    case "m":
        print(f"Nome:{nome}, gender:{gender}")
    case "f":
        print(f"Nome:{nome}, gender:{gender}")
    case _:
        print(f"Impossibile generare un documento d'identità con questo gender '{gender}' ")