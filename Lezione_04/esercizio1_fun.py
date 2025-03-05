def check_value(n:int):
    if n>5:
        print(f"Numero maggiore di 5 = {n}")
    elif n<5:
        print(f"Numero minore di 5 = {n}")
    else:
        print(f"Numero uguale a 5 = {n}")


n:int= int(input("Inserisci un numero da controllare: "))
check_value(n)