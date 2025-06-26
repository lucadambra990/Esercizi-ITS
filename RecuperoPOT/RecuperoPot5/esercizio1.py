import random
def genera(dim:int) -> list[list[int]]:
    mat: list[list[int]] = []
    for r in range(dim):
        row:list = []
        for c in range(dim):
            while True:
                x:int = random.randint(0,13)
                if c == 0: # controlliamo se è uguale a 0 per controllare se è il primo elemento da inserire, poi interrompiamo il ciclo per passare direttamente al controllo successivo
                    row.append(x)
                    break
                if x!=row[0]:
                    row.append(x)
                    break
        mat.append(row)
    return mat

def printMAT(mat:list[list[int]])->list[list[int]]:
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            print(f"{mat[r][c]:<5}", end="")
        print("\n")

def calcolaCarico(mat:list[list[int]],r:int,c:int):
    sr = sum(mat[r])
    sc = 0
    for i in range(len(mat)):
        sc = mat[i][c]
    print(f"k {r},{c} = {sr - sc}")
    return sr -sc

def calcoloNullo(mat:list[list[int]])-> list[tuple[int]]:
    lista_null:list[tuple[int]] = []
    for r in range(len(mat)):
        for c in range(len(mat)):
            z = calcolaCarico(mat,r,c)
            if z == 0:
                lista_null.append((r,c))
        return lista_null
    
def caricoMax(mat:list[list[int]])->tuple[int,int]:
    cMax = 0
    tuple_max:tuple[int,int] = []
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            m = calcolaCarico(mat,r,c)
            if m > cMax:
                cMax = m
                y = list(tuple_max)
                y.append(r,c)
                tuple_max = tuple(y)
        return tuple_max

def caricoMin(mat:list[list[int]])->tuple[int,int]:
    pass

if __name__ == "__main__":
    mat = genera(5)
    printMAT(mat)
    calcolaCarico(mat,2,4)
    print(calcoloNullo(mat))