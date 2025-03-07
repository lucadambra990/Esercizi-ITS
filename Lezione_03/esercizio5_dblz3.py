n:int = int(input("Inserisci un numero: "))

if n%1==0 and n>0:
    s=0
    i=1
    while i<=n: #for i in range(1, n+1) senza i=i+1
        s=s+(i*i)
        i=i+1
    print(f"La somma dei quadrati è {s}")
else:
    print("Errore, n deve essere positivo!")