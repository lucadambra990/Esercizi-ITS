#Dato un numero restituire il suo valore cardinale
# position:int = int(input("Inserisci la posizione in cui ti sei posizionato: "))
# if position == 1:
#     print(f"{position}st!")
# elif position == 2:
#     print(f"{position}nd!")
# elif position == 3:
#     print(f"{position}rd!")
# else:
#     print(f"{position}th!")

#Soluzione col MatchStatement
pos:int = int(input("Inserisci la posizione in cui ti sei posizionato: "))

match pos:
    case 1:
        print(f"{pos}st!")
    case 2:
        print(f"{pos}nd!")
    case 3:
        print(f"{pos}rd!")
    case _:
        print(f"{pos}th!")

#Altro esempio matchStatement
http_status:int = 200

match http_status:
    case 200|201:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500|501:
        print("Server Error")
    case _:
        print("Unknown")

#matchStatement and condintions
n:int = int(input("Insert a number: "))

match n:
    case n if n > 0 and n%2==0:
        print(f"{n} è positivo e pari")
    case n if n > 0 and n%2!=0:
        print(f"{n} è positivo e dispari")
    case n if n < 0 and n%2==0:
        print(f"{n} è negativo e pari")
    case n if n < 0 and n%2!=0:
        print(f"{n} è negativo e dispari")
    case _:
        print("Il numero inserito è 0")

#matchStatement and variables
g:str = input("Inserisci il tuo gender: ")
age:int = int(input("Inserisci la tua età: "))

match(g, age):
    case("f", 5):
        print("Piccola!")
    case("m", 5):
        print("Piccolo!")
    case("f", 10):
        print("Grande!")
    case("m", 10):
        print("Gigante!")
    case _:
        print("Kinder Sorpresa!")

#matchStatement and list
ingredienti:list = ["pomodoro","mozzarella","basilico"]

match ingredienti:
    case["pomodoro", "mozzarella", "basilico"]:
        print("Puoi fare una caprese")
    case["pasta","pomodoro", *_]:
        print("Puoi fare la pasta al pomodoro!")
    case["pane","prosciutto","formaggio"]:
        print("Puoi fare un panino!")
    case _:
        print("Non saprei cosa consigliarti...sperimenta!")

#matchStatement and dictionaries
user:dict = {"nome":"Luca", "ruolo":"admin"}

match user:
    case {"nome":name, "ruolo":"admin"}:
        print(f"Benvenuto amministratore {name}")
    case {"nome":name, "ruolo":"utente"}:
        print(f"Benvenuto utente {name}")
    case _:
        print("Ruolo non riconosciuto")

#matchStatement and tuples
point = (3,5)

match point:
    case (0,0):
        print("Origine")
    case (x, 0):
        print(f"Punto sull'asse X: ({x}, 0)")
    case (0, y):
        print(f"Punto sull'asse Y:(0 ,{y})")
    case _:
        print(f"Punto generico: {point}")