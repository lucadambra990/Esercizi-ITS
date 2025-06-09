def RicercaBinaria(lista:list,target:int)->bool:
    lista1=sorted(lista)
    print(lista1)
    i=0
    v=len(lista1)-1
    while i <= v:
        m=(i+v)//2
        if lista1[m]==target:
            return True
        elif lista1[m]<target:
            i=m+1
        else:
            v=m-1
    return False
    

print(RicercaBinaria([1,2,3,5,8,11,9], 3))