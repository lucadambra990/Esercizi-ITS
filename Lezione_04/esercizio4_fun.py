def check_each(lista:list[int]):
    for i in lista:
        if i > 5:
            print(f"Numero maggiore di 5")
        elif i < 5:
            print(f"Numero minore di 5")
        else:
            print(f"Numero uguale a 5")

lista:list[int] = [1,2,3,5,6,9,80,87,50,21,23,54,13]
check_each(lista)