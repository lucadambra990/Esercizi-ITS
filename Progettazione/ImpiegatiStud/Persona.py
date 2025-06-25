from datetime import date
from myTypes import *
class Persona:
    def __init__(self,nome:str,cognome:str,cf:CodiceFiscale,nascita:date,genere:Genere,maternita:IntGEZ|None=None):
        if genere == "donna":
            pass