def multiply(lista:list[int],threshold:int)->int:
    prodotto:int=1
    for i in lista:
        if i < threshold:
            prodotto*=i
    return prodotto

print(multiply([1,2,3,3,56,5,5,95,95,5,5,89],10))