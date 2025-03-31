class Restaurant:
    
    def __init__(self, name:str, cuisine_type:str, number_served:int):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def displayData(self):
        print(f"Nome: {self.name}\nTipo di cucina: {self.cuisine_type}")


    def openRestaurant(self):
        print(f"{self.name} is open!")

ristorante:Restaurant = Restaurant("Al vecchio capanaccio","mediterranea")
ristorante.openRestaurant()
ristorante.displayData()