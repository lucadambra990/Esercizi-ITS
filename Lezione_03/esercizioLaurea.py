votoLaurea:int = int(input("Inserisci il tuo voto di laurea: "))
scala_america:float = 4.0

match votoLaurea:
    case votoLaurea if votoLaurea >=106 and votoLaurea<=110:
        print(f"Il tuo voto convertito in scala americana è {scala_america}")
    case votoLaurea if votoLaurea >=101 and votoLaurea<=105:
        print(f"Il tuo voto convertito in scala americana è {scala_america - 0.3}")
    case votoLaurea if votoLaurea >=96 and votoLaurea <=100:
        print(f"Il tuo voto convertito in scala americana è {scala_america - 0.6}")
    case votoLaurea if votoLaurea >=91 and votoLaurea <=95:
        print(f"Il tuo voto convertito in scala americana è {scala_america - 1}")
    case votoLaurea if votoLaurea >=86 and votoLaurea <=90:
        print(f"Il tuo voto convertito in scala americana è {scala_america - 1.3}")
    case votoLaurea if votoLaurea >=81 and votoLaurea <=85:
        print(f"Il tuo voto convertito in scala americana è {scala_america - 1.6}")
    case votoLaurea if votoLaurea >=76 and votoLaurea <=80:
        print(f"Il tuo voto convertito in scala americana è {scala_america - 2}")
    case votoLaurea if votoLaurea >=70 and votoLaurea <=75:
        print(f"Il tuo voto convertito in scala americana è {scala_america - 2.3}")
    case votoLaurea if votoLaurea >=66 and votoLaurea <=69:
        print(f"Il tuo voto convertito in scala americana è {scala_america - 3}")
    case _:
        print(f"Il tuo voto inserito non è valido {votoLaurea}")
