def subNum(a:int, b:int):
    result:int = a-b
    return result
a:int=int(input("Inserisci il valore di a: "))
b:int=int(input("Inserisci il valore di b: "))
sub = subNum(a,b)
print(f"La sottrazzione tra i due numeri a e b è {subNum(a,b)}")
print(type(subNum(a,b)))