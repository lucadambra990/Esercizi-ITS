class Persona:
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0

    # funzione che mostri in output tutti i dati di una persona
    def displayData(self) -> None:
        print(f"Nome:{self.name}\nCognome:{self.lastname}\nEtà:{self.age}")

    # mi consente di impostare un valore per self.name
    def setName(self,name:str) ->None:
        self.name = name

    # mi consente di impostare un valore per self.lastname
    def setLastname(self,lastname:str) ->None:
        self.lastname = lastname

    # mi consente di impostare un valore per self.age
    def setAge(self,age:int) ->None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

    # ritorna il valore di set.name
    def getName(self) ->str:
        return self.name
    
    # ritorna il valore di set.lastname
    def getLastname(self) ->str:
        return self.lastname
    
    # ritorna il valore di set.age
    def getAge(self) ->int:
        return self.age

# crea un oggetto di tipo Persona
l:Persona=Persona()

# stampa i dati della Persona creata
l.displayData()
print("------------")
# impostare il nome di una persona
l.setName("Luca")

# impostare il cognome di una persona
l.setLastname("D'Ambra")

# impostare l'età di una persona
l.setAge(21)

# stampa i dati della Persona creata
l.displayData()
print("------------------")
print(l.getName(),l.getLastname(),l.getAge())