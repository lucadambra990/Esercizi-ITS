from abc import ABC,abstractmethod


class Animal:
    def __init__(self,id:str,name:str,age_years:int,weight_kg:float):
        self.id=id
        self.name=name
        self.age_years=age_years
        self.weight_kg=weight_kg

    @abstractmethod
    def species(self):
        pass

    @abstractmethod
    def daily_food_grams(self):
        pass

    def info(self):
        return {"id":self.id,"name":self.name,"species":self.species,"age_years":self.age_years,"weight_kg":self.weight_kg}
    
    def bmi_like(self):
        return self.weight_kg/(self.age_years + 1)
    

class Dog(Animal):
    def __init__(self, id:str, name:str, age_years:int, weight_kg:float,breed:str,is_trained:bool=False):
        super().__init__(id, name, age_years, weight_kg)
        self.breed=breed
        self.is_trained=is_trained

    def species(self):
        return "dog"
    
    def daily_food_grams(self):
        return 200 + (self.age_years * 50)
    
    def info(self):
        return super().info(self.breed,self.is_trained)
    
class Cat(Animal):
    def __init__(self, id:str, name:str, age_years:int, weight_kg:float,favorite_toy:str,indoor_only:bool=False):
        super().__init__(id, name, age_years, weight_kg)
        self.favorite_toy=favorite_toy
        self.indoor_only=indoor_only

    def species(self):
        return "cat"
    
    def daily_food_grams(self):
        return 100 + (self.age_years * 30)
    
    def info(self):
        return super().info(self.favorite_toy,self.indoor_only)
    
class Shelter():
    def __init__(self):
        self.animals:dict[str,Animal]={}
        self.adoptions:dict[str,str]={}

    def add(self,animal:Animal):
        if animal.id in self.animals:
            raise KeyError("Esiste già un'animale con questo id")
        else:
            self.animals["id"]=animal

    def get(self,animal_id):
        if animal_id in self.animals:
            return self.animals[animal_id]
        return None
    
    def list_all(self):
        return [Animal.info() for animal in self.animals.values()]
    
    def is_adopted(self,animal_id):
        if animal_id in self.adoptions:
            return True
        return False
    
    def set_adopted(self,animal_id,adopter_name):
        self.adoptions[animal_id]=adopter_name


Cane:Dog=Dog("1","Bobby",1,2,"Pastore tedesco",False)
Gatto:Cat=Cat("1","Mizzi",3,3.5,"gomitolo",True)