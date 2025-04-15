class Persona:
    def __init__(self,name:str,lastname:str, age:int):
        self.setName(name)
        self.setLastname(lastname)
        self.setAge(age)

     # metodo speciale che ritorna una stringa e che viene chiamata automaticamente quando si usa l'istruzione print(obj),
    # dove obj è un oggetto della classe Persona
    # funzione che mi mostri in output i dati relativi ad una persona 
    def __str__(self) -> str:
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
    
    # il metodo __call__ mi consente di usare l'oggetto della classe Persona istanziato come una funzione.
    # Quindi, un oggetto della classe Persona si comporta come una funzione
    def __call__(self):
        if self.age < 18:
            print(f"{self.name} {self.lastname} e' minorenne!")
        elif 18 <= self.age < 30:
            print(f"{self.name} {self.lastname} e' maggiorenne!")
        elif 30<= self.age < 80:
            print(f"{self.name} {self.lastname} e' una persona adulta!")
        else:
            print(f"{self.name} {self.lastname} e' una persona anziana!")

    # mi consente di impostare un valore per self.name
    def setName(self,name:str) ->None:
        if name:    
            self.name = name
        else:
            print("Errore! La stringa non può essere vuota")
    # mi consente di impostare un valore per self.lastname
    def setLastname(self,lastname:str) ->None:
        if lastname:    
            self.lastname = lastname
        else:
            print("Errore! La stringa non può essere vuota")

    # mi consente di impostare un valore per self.age
    def setAge(self,age:int) ->None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

    # metodi getter

    # ritorna il valore di set.name
    def getName(self) ->str:
        return self.name
    
    # ritorna il valore di set.lastname
    def getLastname(self) ->str:
        return self.lastname
    
    # ritorna il valore di set.age
    def getAge(self) ->int:
        return self.age
