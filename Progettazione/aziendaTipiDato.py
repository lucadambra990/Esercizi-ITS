from myTypes import *
from datetime import date
import re
from typing import Self, Any
from __future__ import annotations

class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # <<immutable>>, # noto alla nascita
    _stipendio: RealGZ # # noto alla nascita
    _progetti:dict[Progetto,str]

    def __init__(self, nome:str, cognome:str, nascita: date, stipendio: RealGZ) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> RealGZ:
        return self._stipendio

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    def set_stipendio(self, stipendio: RealGZ) -> None:
        self._stipendio = stipendio

    def __str__(self) -> str:
        return (f"{self.nome()} {self.cognome()}, "
                f"nascita: {self.nascita()}, "
                f"stipendio: {self.stipendio()}")
    
    def add_progetto(self)->None:
        pass
    


class afferenza:
    _dAfferenza:date
    def __init__(self,dAfferenza:date):
        self._dAfferenza=dAfferenza

    def get_afferenza(self)->date:
        return self._dAfferenza
    
class Progetto:

    _nome: str # noto alla nascita
    _budget: RealGZ # noto alla nascita

    def __init__(self, nome: str, budget: RealGZ) -> None:
        self._nome = nome
        self._budget = budget

    def nome(self) -> str:
        return self._nome

    def budget(self) -> RealGZ:
        return self._budget

    def get_nome(self) -> str:
        return self._nome

    def get_budget(self) -> RealGZ:
        return self._budget

    def __str__(self) -> str:
        return f"Progetto '{self.nome()}' con budget: {self.budget()}€"

    def __repr__(self) -> str:
        return f"Progetto(nome={self.get_nome()}, budget={self.budget()})"
    
    def get_impiegato(self)->str:
        pass
    



class Telefono(str):
    def __new__(cls, tel:str):
        if re.fullmatch(r"^\+?[1-9][0-9]{7,14}$", tel):

            return super().__new__(cls,tel)
        raise Exception(f"Il numero: {tel} inserito non rispetta lo standard")


class Dipartimento:

    _nome: str # noto alla nascita
    _telefoni: set[str] # [1..*] (e quindi noto alla nascita)
    _indirizzo: Indirizzo # mutabile, [0..1], certamente noto alla nascita
    _citta: Citta # noto alla nascita

    def __init__(self, nome: str, telefono: str, indirizzo: Indirizzo,
                 c: Citta) -> None:
        self.set_nome(nome)

        self._telefoni = set()
        self.add_telefono(telefono)

        self.set_indirizzo(indirizzo)
        self.set_citta(c)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def telefoni(self) -> frozenset[str]:
        return frozenset(self._telefoni)
    
    def add_telefono(self, telefono: str) -> None:
        self._telefoni.add(telefono)

    def remove_telefono(self, t: str) -> None:
        if len(self.telefoni()) == 1:
            raise RuntimeError('Il dipartimento deve avere almeno un numero di telefono')
        elif t not in self.telefoni():
            raise KeyError(f"Non posso rimuovere il numero di telefono {t} che non appartiene al dipartimento")

        self._telefoni.remove(t)

    def indirizzo(self) -> Indirizzo:
        return self._indirizzo
    
    def set_indirizzo(self, indirizzo: Indirizzo|None) -> None:
        self._indirizzo = indirizzo

    def remove_indirizzo(self) -> None:
        self.set_indirizzo(None)

    def citta(self) -> Citta:
        return self._citta

    def set_citta(self, c: Citta) -> None:
        self._citta = c

    def __repr__(self) -> str:
        return f'Dipartimento({self._nome}, {self._telefoni}, {self._indirizzo}, {self._citta})'

    def __str__(self) -> str:
        if self.indirizzo():
            ind_str: str = "con sede in " + str(self.indirizzo())
        else:
            ind_str: str = "senza sede"

        tel_str: str = "[" + ", ".join(self.telefoni()) + "]"

        return f"Dipartimento '{self.nome()}' {ind_str} a {self.citta()} e numeri di telefono: {tel_str}"

class Citta:
    _nome: str

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome