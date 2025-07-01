from Persona import Persona
from myTypes import *

class Impiegatp(Persona):
    _stipendio:RealGEZ
    _ruolo:Ruolo
    _is_responsabile:bool|None

    def __init__(self, stipendio:RealGEZ, ruolo:Ruolo, is_responsabile:bool|None = None):
        self.setStipendio(stipendio)
        self.setRuolo(ruolo)

    def setStipendio(self, stipendio:RealGEZ):
        self._stipendio = stipendio

    def setRuolo(self, ruolo:Ruolo):
        self._ruolo = ruolo
     