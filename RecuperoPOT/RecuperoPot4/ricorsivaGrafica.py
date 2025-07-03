def printListBackward(lista:list):
    if lista == []:
        return
    print(lista[-1])
    lista.pop()
    printListBackward(lista)

printListBackward([1,2,3,4,5])