from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nome:str):  
        if len(nome)<2:
            raise ValueError("Il nome deve avere almeno due caratteri")
        
        self._nome = nome.capitalize() # rende la prima lettera maiuscola


from ImpiegatiStud import Persona

class Studente(Persona):
    _matricola:int
    
    def __init__(self, nome:str, matricola:int):
        super().__init__(nome)
        self._matricola = matricola

mario = Studente("Mario",1234) # viene invocato come Persona("mario")

print(type(mario))
print(isinstance(mario,Persona))
print(Studente.mro()) # mro stampa tutta la catena delle eredietarietà

# class Persona:
#     def __init__(self,*,nome:str,is_studente:bool=False,matricola:int|None=None,corso_iscritto:Corso|None=None):
#         if is_studente != matricola is not None or is_studente != corso_iscritto is not None:
#             raise ValueError("...")