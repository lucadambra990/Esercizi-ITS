def baricentro(v:list[int])->int|None:
    for i in range(len(v)):
        if(sum(v[:i+1])) == sum(v[i+1:]):
            print(f"Esiste il baricentro del vettore v={v} ed è dato dall'indice {i}")
    return None

def printResult(v:list[int])->int|None:
    baricentro(v)
    

baricentro([1,2,3,3,2,-1])
printResult([1,2,3,3,2,-1])