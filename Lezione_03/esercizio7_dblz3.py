i=0
s=0
while True:
    opzione:str = input("inserisci un opzione tra si e no: ")
    if opzione == "si":
        voto:int = int(input("Inserisci un voto: "))
        if voto >=0:
            s=s+voto
        else:
            print("Inserisci un voto positivo!")
        i=i+1
    else:
        if i>0:
            print(f"La media dei voti inseriti è {s/i}")
        else:
            print("Non sono stati inseriti voti!")
        break