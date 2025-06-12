from datetime import date
from typing import TYPE_CHECKING
from __future__ import annotations

if TYPE_CHECKING:
    from aziendaTipiDato import Impiegato
    from aziendaTipiDato import Progetto


class coinvolto:

    @staticmethod
    def add(cls,progetto:Progetto,impiegato:Impiegato,data:date):
        l = cls._Link(progetto, impiegato, data)
        progetto._add_link_coinvolto(l)
        impiegato._add_link_coinvolto(l)

    @staticmethod
    def remove(cls,l:_link):
        l.progetto()._remove_link_coinvolto()
        l.impiegato()._remove_link_coinvolto()
        del l




    class _link:
        _impiegato:Impiegato
        _progetto:Progetto
        _data:date

        def __init__(self,impiegato:Impiegato,progetto:Progetto,data:date):
            self._impiegato = impiegato
            self._progetto = progetto
            self._data = data

        def impiegato(self)->Impiegato:
            return self._impiegato
        
        def progetto(self)->Progetto:
            return self._progetto
        
        def data(self)->date:
            return self._data