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


print(lista)

occ=0
for i in lista:
    pass

for i in lista:
    if x in lista:
        print(f"Il numero {x} compare la prima volta nella lista nella posizione {lista.index(x)}")
        break

somma=0
for sm in lista:
    if sm!=x:
        somma+=sm
print(f"La somma dei numeri diversi da {x} è {somma}")

