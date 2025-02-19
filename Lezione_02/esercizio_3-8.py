#Esercizio 3-8
travelPlace:list[str] =["India","Tokyo","Thailandia","Dubai","Svizzera","Lisbona"]
print(travelPlace)

#Stampe delle diverse ordinazioni della lista
print(f"Lista in ordine alfabetico senza modificarla{sorted(travelPlace)}")
print(f"lista originale {travelPlace}")
print(f"Lista invertita senza modificarla{sorted(travelPlace, reverse=True)}")
print(f"lista originale {travelPlace}")

travelPlace.sort()
print(f"Lista ordinata in ordine alfabetico ma modificandola{travelPlace}")
print(f"lista originale ma modificata{travelPlace}")
travelPlace.sort(reverse=True)
print(f"lista invertita ma modificandola{travelPlace}")
print(f"lista originale ma modificata{travelPlace}")
travelPlace.reverse()
print(f"lista invertita ma modificandola{travelPlace}")
print(f"lista originale ma modificata{travelPlace}")
print(travelPlace)