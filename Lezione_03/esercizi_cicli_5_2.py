from typing import Any
color:str = input("Inserisci un colore: ")
num:int = int(input("Inserisci un numero da 1 a 10: "))
list_cose:list[Any] = [1,2,3,4,5,6,7,8,9,10]
predict:bool

if color == "yellow":
    predict=True
    print(f"Il colore inserito è yellow? {predict}")
else:
    predict=False
    print(f"Il colore inserito è yellow? {predict}")

if color == "red".lower():
    predict=True
    print(f"{color.lower()} == color? {predict}")
else:
    predict=False
    print(f"Predict {predict}")

if num > 6:
    predict=True
    print(f"Il numero inserito {num} è maggiore di 6? {predict}") 
else:
    predict=False
    print(f"Il numero inserito {num} è maggiore di 6? {predict}")

if num < 5:
    predict=True
    print(f"Il numero inserito {num} è minore di 5? {predict}") 
else:
    predict=False
    print(f"Il numero inserito {num} è minore di 5? {predict}")

if num >= 3:
    predict=True
    print(f"Il numero inserito {num} è maggiore o uguale a 3? {predict}") 
else:
    predict=False
    print(f"Il numero inserito {num} è maggiore o uguale a 3? {predict}")

if num <=8:
    predict=True
    print(f"Il numero inserito {num} è minore o uguale a 8? {predict}") 
else:
    predict=False
    print(f"Il numero inserito {num} è minore o uguale a 8? {predict}")

if num > 6 or num <3:
    predict=True
    print(f"Il numero inserito {num} è maggiore di 6 o minore di 3? {predict}") 
else:
    predict=False
    print(f"Il numero inserito {num} è maggiore di 6 o minore di 3? {predict}")

if num > 2 and num <9:
    predict=True
    print(f"Il numero inserito {num} è maggire di 2 e minore di 9? {predict}") 
else:
    predict=False
    print(f"Il numero inserito {num} è maggiore di 2 o minore di 9? {predict}")

if 1 in list_cose:
    predict=True
    print(f"Il numero 1 è presente nella lista? {predict}")
elif 21 not in list_cose:
    predict=True
    print(f"Il numero 21 non è presente nella lista? {predict}")