from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_model.nazione import Nazione


class Citta:
    _nome:str
    _abitanti:int
    _nazione:Nazione

    def __init__(self,nome:str,abitanti:int,nazione:Nazione):
        self.set_nome(nome)
        self.set_abitanti(abitanti)
        self.set_nazione(nazione)

    def nome(self)->str:
        return self._nome
    
    def abitanti(self)->int:
        return self._abitanti
    
    def set_nome(self,nome:str)->None:
        self._nome = nome

    def set_abitanti(self,abitanti:int)->None:
        self._abitanti = abitanti

    def nazione(self)-> Nazione:
        return self._nazione
    
    def set_nazione(self,nazione:Nazione)->None:
        try:
            self.nazione()._remove_citta(self)
        except AttributeError:
            pass

        self._nazione = nazione
        nazione._add_citta(self)

    def __repr__(self)->str:
        return f"Citta(nome='{self.nome()}', abitanti='{self.abitanti()}', nazione='{self.nazione()}')"