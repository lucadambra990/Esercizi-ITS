from myTypes import *
from datetime import datetime
import re
from typing import Self, Any

class Impiegato:
    _nome:str
    _cognome:str
    _nascita:datetime
    _stipendio:RealGZ
    def __init__(self,nome:str,cognome:str,nascita:datetime,stipendio:RealGZ):
        self._nome=nome
        self._cognome=cognome
        self._nascita=nascita
        self._stipendio=stipendio
    
    def get_nome(self)->str:
        return self._nome
    
    def get_cognome(self)->str:
        return self._cognome
    
    def get_nascita(self)->datetime:
        return self._nascita
    
    def get_stipendio(self)->float:
        return self._stipendio
    


class afferenza:
    _dAfferenza:datetime
    def __init__(self,dAfferenza:datetime):
        self._dAfferenza=dAfferenza

    def get_afferenza(self)->datetime:
        return self._dAfferenza
    
class Progetto:
    _nome:str
    _budget:RealGZ
    def __init__(self,nome:str,budget:RealGZ):
        self._nome=nome
        self._budget=budget
    
    def get_nome(self)->str:
        return self._nome
    
    def get_budget(self)->float:
        return self._budget
    



class Telefono(str):
    def __new__(cls, tel:str):
        if re.fullmatch(r"^\+?[1-9][0-9]{7,14}$", tel):

            return super().__new__(cls,tel)
        raise Exception(f"Il numero: {tel} inserito non rispetta lo standard")


class Dipartimento:
    _nome:str
    _telefono:set[Telefono]
    _indirizzo:Indirizzo
    
    def __init__(self,nome:str,telefono:Telefono,indirizzo:Indirizzo):
        self._nome=nome
        self._telefono=telefono
        self._indirizzo=indirizzo

    def get_nome(self)->str:
        return self._nome
    
    def set_nome(self,nome:str)->None:
        self._nome=nome
    
    def get_telefono(self)->frozenset[Telefono]:
        return frozenset(self._telefono)

    def add_telefono(self, new_telefono:str)->None:
        self._telefono.add(new_telefono)

    def remove_telefono(self,t:str)->None:
        if len(self.Telefono())>1:
            self._telefono.remove(t)
        else:
            raise RuntimeError("Il dipartimento deve avere almeno un numero di telefono")

    def get_indirizzo(self)->Indirizzo:
        return self._indirizzo

    def set_indirizzo(self,indirizzo:Indirizzo)->None:
        self._indirizzo=indirizzo

    def remove_indirizzo(self)->None:
        self.set_indirizzo(None)