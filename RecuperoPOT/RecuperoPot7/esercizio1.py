def baricentro(v:list[int])->int|None:
    for i in range(len(v)):
        if(sum(v[:i+1])) == sum(v[i+1:]):
            print(f"Esiste il baricentro del vettore v={v} ed è dato dall'indice {i}")
    return None

def printResult(v:list[int])->int|None:
    baricentro(v)
    if baricentro is None:
        print(f"Il baricentro del vettore v={v} non esiste")
    else:
        print(f"Il baricentro del vettor v={v} esiste ed è dato dall'indice i")
