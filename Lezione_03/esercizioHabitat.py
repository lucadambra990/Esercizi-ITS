from typing import Any
habitat:list = ["terra","aria","acqua"]
animale:str = input("Inserisci un animale: ")
animal_type:str

animalDict:dict[str, Any] = {"animale":animale,"tipo":animal_type, "habitat":habitat}

match animalDict:
    #mammiferi
    case{"animale":animale,"tipo":"mammiferi","habitat":habitat} if habitat in ["terra","acqua"]:
        match animale:
            #habitat terra
            case animale if animale in ["cane","gatto","cavallo","elefante","leone"] and habitat == "terra":
                print(f"L'animale {animale} è uno dei mammiferi che può vivere sulla terra!")
            #habitat acqua
            case animale if animale in ["balena","delfino"] and habitat == "acqua":
                print(f"L'animale {animale} è uno dei mammiferi che può vivere in acqua!")
            #default case
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")