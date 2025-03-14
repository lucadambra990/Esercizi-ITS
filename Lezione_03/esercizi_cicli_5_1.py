macchina:str = input("Inserisci un modello di una macchina: ")
predict:bool

if macchina == "BMW":
    predict = True
    print(f"{macchina} == macchina? {predict}")
elif macchina == "Audi":
    predict = True
    print(f"{macchina} == macchina? {predict}")
elif macchina == "Ferrari":
    predict = True
    print(f"{macchina} == macchina? {predict}")
elif macchina == "KTM":
    predict = False
    print(f"{macchina} == macchina? {predict}")
elif macchina == "BMX":
    predict = False
    print(f"{macchina} == macchina? {predict}")
elif macchina == "Skateboard":
    predict = False
    print(f"{macchina} == macchina? {predict}")
else:
    print(f"L'elemento inserito '{macchina}' non è presente nell'elenco")