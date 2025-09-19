from Persona import *

class Paziente(Persona):
    _codice:int
    def __init__(self, first_name, last_name,IdCode:int,age:int):
        super().__init__(first_name, last_name)
        self.setAge(age)
        self.setIdCode(IdCode)

    def setIdCode(self,IdCode:int):
        self._codice=IdCode

    def getIdCode(self):
        return self._codice
    
    def patientInfo(self):
        print(f"Paziente: {Persona.getName(self)} {Persona.getLastName(self)}\nID:{self._codice}")


if __name__ == "__main__":
    paziente:Paziente = Paziente("Luca","Polaso",1111,23)
    paziente.patientInfo()