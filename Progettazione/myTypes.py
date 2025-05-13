from typing import Self, Any
from enum import *

class Genere(StrEnum):
    uomo = auto()
    donna = auto()


class Continente(StrEnum):
    asia = auto()
    europa = auto()
    america = auto()
    africa = auto()
    antartide = auto()









class Persona:

    nome:str
    cf:str

    def __new__(cls, *args, **kwargs) -> Self:
        return super().__new__(cls)
    
    def __init__(self,nome:str,cf:str)->None:
        self.nome=nome
        self.cf=cf

    def __eq__(self, other:Any):
        if not isinstance(other, Persona):
            return False
        return self.cf==other.cf
    
    def __hash__(self)->int:
        return hash(self.cf)
    
    def __repr__(self):
        return f'Persona({self.cf}) e nome {self.nome}'


class Voto(int):
    def __new__(cls, v:int|float|Self)->Self:
        if v < 18 or v > 30:
            raise ValueError(f"Value v=={v} deve essere compreso tra 18 e 30")
        return int.__new__(cls,v)
    

class IntGEZ(int):
    def __new__(cls, v:int|float|Self)->Self:
        if v < 0:
            raise ValueError(f"Value v=={v} deve essere compreso tra 18 e 30")
        return int.__new__(cls,v)
    
class RealGZ(float):
    pass

class CodiceFiscale(str):
    def __new__(cls, cf)->Self:
        pass # controllare se cf sia uguale alle regEx




class Indirizzo:
    _via:str
    _civico:int

    def __init__(self, via:str,civico:int)->None:
        self._via = via
        self._civico = civico

    def via(self)->str:
        return self._via
    
    def civico(self)->int:
        return self._civico
    
    # non vogliamo che vengano modificati i valori di via e indirizzo,
    # rendendo private le due variabili con _ 
    # e non implementando i metodi setter nella funzione

    def __hash__(self)->int:
        return hash((self._via, self._civico))
    
    def __eq__(self, other:Any)->bool:
        if other in  None or \
            not isinstance(other, Indirizzo) or \
                hash(self)!=hash(other):
            return False
        return self._via == other._via and self._civico == other._civico






if __name__ == '__main__':
    # Test dei tipi qui definiti
    print(Genere.uomo) # posso usare metodi upper lower ecc.. e come tipo ritorna enum 'Genere'
    print(Genere.donna)

    print(Continente.america.capitalize())


    indirizzo1:Indirizzo = Indirizzo("via",34)
    indirizzo1:Indirizzo = Indirizzo("via2",36)

    alice1:Persona = Persona ("Alice","AA")
    print(type(alice1))
    print("Superclasse di persona" + str(Persona.mro()[-1])) # mro: lista di tipi e supertipi della classe
    
    alice2:Persona = Persona("Alessia", "AA")