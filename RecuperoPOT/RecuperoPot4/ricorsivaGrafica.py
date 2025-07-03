def printListBackward(lista:list):
    if lista == []:
        return
    print(lista[-1])
    lista.pop()
    printListBackward(lista)