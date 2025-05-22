import re
from typing import Self, Any

class CodiceFiscale:
    _cf=r"([A-Z]{6}[0-9LMNPQRSTUV]{2}[ABCDEHLMPRST]{1}[0-9LMNPQRSTUV]{2}[A-Z]{1}[0-9LMNPQRSTUV]{3}[A-Z]{1})$|([0-9]{11})$"
    def __init__(self, codice)->None:
        codice = codice.upper()
        if not re.findall(self._cf, codice):
            raise ValueError(f"Codice fiscale non valido {codice}")
        self._cf = codice

    def cf(self)->str:
        return self._cf
    
    def __hash__(self)->int:
        return hash(self._cf)
    
    def __str__(self)->str:
        return f"Codice Fiscale: {self._cf}"
    


class Iscrizione:
    def __new__(anno:int|Self)->Self:
        if anno < 1900:
            raise ValueError(f"L'anno d'iscrizione deve essere maggiore di 1900")
        return int.__new__(anno)
    

class Corso:
    def __new__(cls,num_min:int|Self)->Self:
        if num_min < 0:
            raise ValueError(f"Il tempo del corso non può essere minore di 0")
        return int.__new__(cls,num_min)