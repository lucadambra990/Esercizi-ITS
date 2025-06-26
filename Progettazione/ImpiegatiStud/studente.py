from Persona import Persona

class Studente(Persona):
    _matricola:int
    def __init__(self, matricola:int)->None:
       if matricola is None:
           raise ValueError("La matricola non può essere None")
       elif not matricola:
           raise ValueError("La matricola non può esseere vuota")
       
    def __hash__(self) -> int:
        return hash((self._matricola))


    def __eq__(self, value)-> bool:
        if value is None or \
            not isinstance(value, Studente) or \
                hash(self)!=hash(value):
            return False
        return self._matricola == value._matricola
    
    def get_Matricola(self)->int:
        return self._matricola