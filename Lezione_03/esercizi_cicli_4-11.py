lista_pizza:list[str] = ["Margherita","Diavola","Quattro formaggi"]
friend_pizzas:list[str] = ["Margherita","Diavola","Quattro formaggi"]
lista_pizza.append("Er Crostino")
friend_pizzas.append("Boscaiola")

for i in lista_pizza:
    print(f"Le mie pizze preferite sono {i}")
for i in friend_pizzas:
    print(f"Le pizze preferite dei miei amici sono {i}")