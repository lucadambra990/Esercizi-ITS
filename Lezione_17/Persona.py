class Persona:
    _first_name:str
    _last_name:str
    _age:int
    def __init__(self, first_name: str, last_name: str):
        if isinstance(first_name, str):
            self._first_name = first_name
        else:
            self._first_name = None
            print("Il nome inserito non è una stringa!")
        if isinstance(last_name, str):
            self._last_name = last_name
        else:
            self._last_name = None
            print("Il cognome inserito non è una stringa!")
        if isinstance(self._first_name, str) and isinstance(self._last_name, str):
            self._age = 0
        else:
            self._age = None

    def setName(self,first_name):
        if isinstance(first_name,str):
            self._first_name=first_name
        else:
            raise TypeError(f"{first_name} non è una stringa!")
    
    def setLastName(self,last_name):
        if isinstance(last_name,str):
            self._last_name=last_name
        else:
            raise TypeError(f"{last_name} non è una stringa!")
    
    def setAge(self,age):
        if isinstance(age,int):
            self._age=age
        else:
            raise TypeError(f"{age} non è un intero!")
    
    def getName(self):
        return self._first_name
    
    def getLastName(self):
        return self._last_name
    
    def getAge(self):
        return self._age
    
    def greet(self):
        print(f"Ciao sono {self._first_name} {self._last_name}! Ho {self._age} anni!")
