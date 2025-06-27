from datetime import date
from myTypes import *
from posizioneMili import *
class Persona:
    _genere: Genere
    _maternita: IntGEZ|None
    _posizione_militare:posMil|None
    _nome:str
    _cognome:str
    _codice_fiscale:CodiceFiscale
    _dataNascita:date

    def __init__(self,nome:str,cognome:str,cf:CodiceFiscale,nascita:date,genere:Genere,maternita:IntGEZ|None=None,posMil:posMil|None=None):
        if genere == Genere.donna:
            if maternita is None:
                raise ValueError("Tutte le donne devo avere un numero di maternità")
            else:
                self._maternita = maternita
        else:
            self._posizione_militare = posMil
        

    def diventa_donna(self, maternita: IntGEZ) -> None:
        self._maternita = maternita
        self.__dimentica_uomo()

    def __dimentica_uomo(self):
        self._posizione_militare = None

    def diventa_uomo(self, posMil:posMil)-> None:
        self._posizione_militare = posMil
        self.__dimentica_donna()

    def __dimentica_donna(self):
        self._maternita = None

    def set_nome(self,nome:str)->None:
        self._nome = nome

    def set_cognome(self,cognome:str)->None:
        self._cognome = cognome

    def set_codiceFiscale(self,cf:CodiceFiscale)->None:
        self._codice_fiscale = cf

    def set_dataNascita(self,nascita:date)->None:
        self._dataNascita = nascita

    def get_nome(self)->str:
        return self.set_nome()
    
    def get_cognome(self)->str:
        return self.set_cognome()
    
    def get_codiceFiscale(self)->str:
        return self.set_codiceFiscale()
    
    def get_dataNascita(self)->str:
        return self.set_dataNascita()
    
    

    
