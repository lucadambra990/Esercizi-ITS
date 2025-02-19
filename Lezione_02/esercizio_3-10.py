# #Esercizio 3-10
mountain_list:list[str] = ["Everest", "Kilimangiaro", "Monte Bianco", "K2"]
print("Aggiunta di un elemento alla fine della lista con append")
mountain_list.append("Epomeo")
print(mountain_list)

print("Aggiunta di un elemento in un indice stabilito con insert")
mountain_list.insert(2, "K12")
print(mountain_list)

print("Rimozione di un elemento tramite indice con pop")
mountain_list.pop(3)
print(mountain_list)

print("Rimozione di un elemento tramite remove")
mountain_list.remove("Everest")
print(mountain_list)

print("Estendere la lista con un'altra lista con extend")
mountain_list2:list = ["Makalu", "Shishapangma", "Nanga Parbat"]
mountain_list.extend(mountain_list2)
print(mountain_list)

print("Ordinazione della lista con i metodi sort, sorted, reverse")
print(f"Lista sistemata con il metodo sorted {sorted(mountain_list)}")
mountain_list.sort()
print(f"Lista sistemata con il metodo sort {mountain_list}")
mountain_list.reverse()
print(f"Lista sistemata con il metodo reverse {mountain_list}")

print("Eliminazione della lista tramite del")
del mountain_list2[0]
del mountain_list2[1]
del mountain_list[0]
del mountain_list[1]
print(mountain_list)
print(mountain_list2)