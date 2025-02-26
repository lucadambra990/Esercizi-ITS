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


#Questo ciclo for permette di stampare i numeri da 1 a 20 (nelle parentesi c'è 21 perché la funzione range prende il valore finale, in questo caso 21, e lo fa -1)
# for i in range(1,21):
#     print(i)



#Inizializzo la lista vuota da riempire
# list_number2:list = [

# ] 
#Tramite questo ciclo for stampiamo i numeri da 1 ad 1000000, usando la funzione append per inserire i numeri iterati tramite il contatore i nella nostra lista
# for i in range(1,1000001):
#     list_number2.append(i)
#     print(list_number2)