#Esercizio 3-8
travelPlace:list =["India","Tokyo","Thailandia","Dubai","Svizzera","Lisbona"]
print("Vorrei andare a " + travelPlace[0])
print("Vorrei andare a " + travelPlace[1])
print("Vorrei andare a " + travelPlace[2])
print("Vorrei andare a " + travelPlace[3])
print("Vorrei andare a " + travelPlace[4])
print("Vorrei andare a " + travelPlace[5])

#Stampe delle diverse ordinazioni della lista
print(sorted(travelPlace))
print(sorted(travelPlace, reverse=True))

travelPlace.sort()
print(travelPlace)
travelPlace.sort(reverse=True)
print(travelPlace)

travelPlace.reverse()
print(travelPlace)