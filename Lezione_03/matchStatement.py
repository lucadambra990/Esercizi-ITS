#Dato un numero restituire il suo valore cardinale
position:int = int(input("Inserisci la posizione in cui ti sei posizionato: "))
if position == 1:
    print(f"{position}st!")
elif position == 2:
    print(f"{position}nd!")
elif position == 3:
    print(f"{position}rd!")
else:
    print(f"{position}th!")