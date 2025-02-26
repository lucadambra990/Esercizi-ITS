lista_pizza:list[str] = [
            "Margherita","Diavola","Quattro formaggi"
                    ] #lista delle mie pizze preferite
friend_pizzas:list[str] = [
                "Margherita","Diavola","Quattro formaggi"
                            ] #lista delle pizze preferite dei miei amici
lista_pizza.append("Er Crostino") #con append inserisco un nuovo elemento alla fine della lista
friend_pizzas.append("Boscaiola")
#Utilizzo dei cicli for per iterare ogni elemento delle liste e stampare ogni elemento con la frase nei print
for i in lista_pizza:
    print(f"Le mie pizze preferite sono {i}")
for i in friend_pizzas:
    print(f"Le pizze preferite dei miei amici sono {i}")