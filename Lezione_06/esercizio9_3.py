class User():
    def __init__(self, first_name:str, last_name:str, age:int, birthDate:str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthDate = birthDate
    def displayData(self) ->None:
        print(f"Nome: {self.first_name}\nCognome: {self.last_name}\n Età:{self.age}\n Data di nascita: {self.birthDate}")
    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}")

luca:User = User("Luca","D'Ambra",21,"21/04/2003")
manuel:User = User("Emanuel","Napoleone",21,"21/08/2003")

luca.displayData()
luca.greet_user()
print("-------------")
manuel.displayData()
manuel.greet_user()