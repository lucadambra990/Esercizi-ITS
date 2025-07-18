x = int(input("Inserisci un numero: "))
lista:list=[]
while True:
    s = int(input("Inserisci una sequenza di numeri: "))
    if s == 0:
        break
    else:
        lista.append(s)
    try:
        not isinstance(x,int) and not isinstance(s,int)
    except ValueError as error:
        print(f"{error}, puoi inserire solo numeri interi positivi! ")
# esercizio fatto ma da fare con due funzioni, una che controlla x e faccia il controllo se è valido

print(lista)

occ=0
for i in lista:
    if i == x:
        occ+=1
print(f"Il numero {x} si ripete {occ} volte")

for i in lista:
    if x in lista:
        print(f"Il numero {x} compare la prima volta nella lista nella posizione {lista.index(x)}")
        break

somma=0
for sm in lista:
    if sm!=x:
        somma+=sm
print(f"La somma dei numeri diversi da {x} è {somma}")

