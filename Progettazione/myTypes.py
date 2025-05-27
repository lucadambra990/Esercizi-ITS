from typing import Self, Any
from enum import *
import re

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
    def __new__(cls,v:float|int|str|bool|Self)->Self:
        n:float=float.__new__(cls,v)
        if n>=0:
            return n
        raise ValueError(f"Il valore {n} è negativo!")

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

class Valuta:
    def __new__(cls, v:str):
        if re.fullmatch(r"^[A-Z]{3}$",v):
            return super().__new__(cls,v)
        raise ValueError(f"La stringa {v} non è un codice valido")



class Denaro:
    '''
        Rappresenta il tipo di dato concettuale composto
        con i seguenti campi:
        - importo: Reale
        - valuta: Valuta
    '''
    _importo:float
    _valuta:float

    def __init__(self, imp:float, val:Valuta):
        self._importo = imp
        self._valuta = val

    def importo(self)->float:
        return self._importo
    
    def valuta(self)->Valuta:
        return self._valuta
    
    def __str__(self):
        return f"{self.importo()} {self.valuta()}"
    
    def __repr__(self):
        return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"

    def __hash__(self):
        return hash( (self.importo(), self.valuta()))
    
    def __eq__(self, other:Any)->bool:
        if not isinstance(other, type(self)) or \
            hash(self)!=hash(other):
            return False
        return self.importo() == other.importo and \
            self.valuta() == other.valuta()
    
    def __add__(self, other:Self)->Self:
        '''
        Somma self ad un'altra istanza di Denaro,
        ma solo se la valuta è la stessa.
        Restituisce una nuova istanza di Denaro
        '''
        if self.valuta() != other.valuta():
            raise ValueError(f"Non posso sommare importi di diversa valuta")
        somma:float = self.importo() + other.importo()
        return Denaro(somma, self.valuta())

class FloatDenaro(float):
    pass



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