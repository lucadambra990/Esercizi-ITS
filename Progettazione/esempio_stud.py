from __future__ import annotations
from typing import Any


class Studente:
    _nome:str
    _esami:dict[Modulo, Esame] # da assoc 'esame' [0..*]

    def __init__(self,nome:str):
        self._nome=nome

    def nome(self)->str:
        return self._nome
    
    def set_nome(self,nome:str)->None:
        self._nome=nome

    def esami(self)->frozenset[Esame]:
        return frozenset(self._esami)
    
    def esame(self,modulo:Modulo)->Esame:
        return self._esami[modulo]

    def add_esame(self,modulo:Modulo,voto:int)->None:
        if modulo in self._esami:
            raise KeyError(f"Lo studente {self._nome} ha già superato il modulo {modulo._codice}")
        l:Esame=Esame(self,modulo,voto)
        self._esami[modulo]=voto


    def remove_esame(self,modulo:Modulo)->None:
        if modulo not in self._esami:
            raise KeyError(f"Lo studente non ha mai superato il modulo")
        del self._esami[modulo]

    def remove_link_esame(self,esame:Esame)->None:
        if esame.studente()!=self:
            raise ValueError(f"Il link non è relativo a {self.nome()}ma a {esame.studente()}")
        del self._esami[esame.modulo()]

    def __repr__(self)->str:
        return f"Studente({self.nome()})"

class Modulo:
    _codice:str



class Esame:
    _studente:Studente
    _modulo:Modulo
    _voto:int

    def __init__(self,studente:Studente,modulo:Modulo,voto:int):
        self._studente=studente
        self._modulo=modulo
        self._voto=voto

    def voto(self)->int:
        return self._voto
    
    def studente(self)->Studente:
        return self._studente
    
    def modulo(self)->Modulo:
        return self._modulo