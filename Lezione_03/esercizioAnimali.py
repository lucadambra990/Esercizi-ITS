# mammiferi:list[any]= ["cane", "gatto", "cavallo", "elefante","leone"]
# rettili:list[any] = ["serpente", "lucertola","tartaruga", "coccodrillo"]
# uccelli:list[any] = ["aquila","pappagallo","gufo","falco"]
# pesci:list[any] = ["squalo","trota","salmone","carpa"]

# animale:str = input("Inserisci un animale: ")

# match animale:
#     case animale if animale in mammiferi:
#         print(f"Il {animale} è un mammifero")
#     case animale if animale in rettili:
#         print(f"Il {animale} è un rettile")
#     case animale if animale in uccelli:
#         print(f"Il {animale} è un uccello")
#     case animale if animale in pesci:
#         print(f"Il {animale} è un pesce")
#     case _:
#         print("Categoria sconosicuta")


#metodo alternativo
animale:str = input("Inserisci un animale: ")

match animale:
    case animale if animale in ["cane", "gatto", "cavallo", "elefante","leone"]:
        print(f"Il {animale} è un mammifero")
    case animale if animale in ["serpente", "lucertola","tartaruga", "coccodrillo"]:
        print(f"Il {animale} è un rettile")
    case animale if animale in ["aquila","pappagallo","gufo","falco"]:
        print(f"Il {animale} è un uccello")
    case animale if animale in ["squalo","trota","salmone","carpa"]:
        print(f"Il {animale} è un pesce")
    case _:
        print("Categoria sconosicuta")