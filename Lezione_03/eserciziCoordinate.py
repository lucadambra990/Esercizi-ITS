X:int = int(input("Inserire il valore della coordinata X: "))
Y:int = int(input("Inseirire il valore della coordinata Y: "))
coordinate:tuple[int, int] = (X,Y)

match coordinate:
    case (0,0):
        print("Questo punto è l'origine")
    case (X,Y) if Y==0:
        print("Il punto si trova sull'asse X")
    case(X,Y) if X==0:
        print("Il punto si trova sull'asse Y")
    case (X,Y) if X>0 and Y>0:
        print("Il punto si trova sul primo quadrante")
    case (X,Y) if X<0 and Y>0:
        print("Il punto si trova nel secondo quadrante")
    case(X,Y) if X<0 and Y<0:
        print("Il punto si trova nel terzo quadrante")
    case(X,Y) if X>0 and Y<0:
        print("Il punto si trova nel quarto quadrante")
    case _:
        print("Errore della sintassi")