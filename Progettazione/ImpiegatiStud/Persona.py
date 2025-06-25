from datetime import date
from myTypes import *
from posizioneMili import *
class Persona:
    _genere: Genere
    _maternita: IntGEZ|None
    _posizione_militare:posMil

    def __init__(self,nome:str,cognome:str,cf:CodiceFiscale,nascita:date,genere:Genere,maternita:IntGEZ|None=None):
        if genere == Genere.donna:
            if maternita is None:
                raise ValueError("Tutte le donne devo avere un numero di maternità")
            else:
                self._maternita = maternita
        else:
            pass

    def diventa_donna(self, maternita: IntGEZ) -> None:
        self._maternita = maternita
        self.__dimentica_uomo()

    def __dimentica_uomo(self):
        self._posizione_militare = None
