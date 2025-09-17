from Persona import *

class Dottore(Persona):
    _specializzazione:str
    _parcella:float
    def __init__(self, first_name:str, last_name:str,age:int, specializzazione:str, parcella:float):
        super().__init__(first_name,last_name)
        self.setAge(age)
        self.setSpecialization(specializzazione)
        self.setParcel(parcella)
        
    def setSpecialization(self, specialization):
        if isinstance(specialization,str):
            self._specializzazione = specialization
        else:
            raise TypeError(f"La specializzazione inserita: {specialization} non è una stringa!")
    
    def setParcel(self,parcel):
        if isinstance(parcel,float):
            self._parcella = parcel
        else:
            raise TypeError(f"La parcella inserita: {parcel} non è un float!")
    
    def getSpecializzazion(self):
        return f"La specializzaione è {self._specializzazione}"
    
    def getParcel(self):
        return f"La parcella del dottore è {self._parcella}"
    
    def isAValidDoctor(self):
        if self._age > 30:
            print(f"Il Dottore {self._first_name} {self._last_name} è un dottore valido")
        else:
            print(f"Il Dottore {self._first_name} {self._last_name} non è un dottore valido")

    def doctorGreet(self):
        Persona.greet(self)
        print(f"Sono un medico {self.getSpecializzazion()}")

if __name__ == "__main__":
    dottore:Dottore = Dottore("Luca","D'Ambra",22,"Ginecologo",150.3)
    dottore.isAValidDoctor()
    dottore.doctorGreet()
    print(dottore.getSpecializzazion())
    print(dottore.getParcel())
   
