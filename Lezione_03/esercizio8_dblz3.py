s=0
a:int = int(input("Inserisci il valore di a: "))
b:int = int(input("Inserisci il valore di b: "))
if a>0 and b>a:
    for i in range(a,b+1):
        s=s+a
        a+=1
    print(f"La somma dei numeri tra a e b è {s}")
else:
    print("Errore!")