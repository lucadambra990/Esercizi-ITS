from myTypes import *
from typing import Self, Any






class Volo:
    _codice:str
    _durata_minuti:int
    def __init__(self,codice:str, durata_minuti:int) -> None:
        if codice is None:
            raise TypeError("Il codice non può essere None")
        elif not codice:
            raise ValueError("Il codice non può essere vuoto")
        else:
            self._codice = codice
        self.set_durata_minuti(durata_minuti)


    def __hash__(self) -> int:
        return hash((self._codice, self._durata_minuti))


    def __eq__(self, value)-> bool:
        if value is None or \
            not isinstance(value, Volo) or \
                hash(self)!=hash(value):
            return False
        return self._codice == value._codice and self._durata_minuti == value._durata_minuti
   
    # l'attributo codice è immutabile: il metodo set_codice non dovrebbe esserci!
    '''
    def set_codice(self, codice:str) -> None:
        if not codice:
            raise ValueError("Il codice non può essere vuoto")
        else:
            self._codice = codice'''


    def set_durata_minuti(self, durata_minuti:int) -> None:
        if durata_minuti < 0:
            raise ValueError("La durata non può essere negativa")
        else:
            self._durata_minuti = durata_minuti


    def get_codice(self) -> str:
        return self._codice
   
    def get_durata_minuti(self) -> int:
        return self._durata_minuti
   
class CodiceVolo(str):
    # Gli oggetti di questa classe sono stringhe 
        # che rispettano il formato dei codici dei voli: XY1234
    pass

class Aereoporto:
    _nome:str
    _codice:str
    def __init__(self, nome:str, codice:str) -> None:
        self._nome = nome
        self._codice = codice


    def __hash__(self) -> int:
        return hash((self._nome, self._codice))


    def __eq__(self, value)-> bool:
        if value in  None or \
            not isinstance(value, Aereoporto) or \
                hash(self)!=hash(value):
            return False
        return self._nome == value._nome and self._codice == value._codice
   
   
    def set_nome(self, nome:str) -> None:
        if not self._nome:
            raise ValueError("Nome non può essere vuoto")
        else:
            self._nome = nome


    def set_codice(self, codice:str) -> None:
        if not codice:
            raise ValueError("Il codice non può essere vuoto")
        else:
            self._codice = codice


    def get_nome(self) -> str:
            return self._nome
   
    def get_codice(self) -> str:
        return self._codice
    
class CodiceIATA(str):
    pass
   
class Compagnia:
    _nome:str
    _fondazione:int


    def __init__(self,nome:str,fondazione:int):
        self._nome=nome
        self._fondazione=fondazione


    def __hash__(self) -> int:
        return hash((self._nome, self._fondazione))


    def __eq__(self, value)-> bool:
        if value in  None or \
            not isinstance(value, Compagnia) or \
                hash(self)!=hash(value):
            return False
        return self._nome == value._nome and self._fondazione == value._fondazione
   
    def set_nome(self,nome:str)->None:
        if not self._nome:
            raise ValueError("Il nome non può essere vuoto")
        else:
            self._nome=nome


    def set_fondazione(self,fond:int):
        if self._fondazione < 0:
            raise ValueError("L'anno della fondazione non può essere 0 o negativo")
        else:
            self._fondazione=fond


    def get_nome(self)->str:
        return self._nome
   
    def get_fondazione(self)->int:
        return self._fondazione
   
class Citta:
    _nome:str
    _numAbitanti:int


    def __init__(self,nome:str,numAbitanti:int):
        self._nome=nome
        self._numAbitanti=numAbitanti


    def __hash__(self) -> int:
        return hash((self._nome))


    def __eq__(self, value)-> bool:
        if value in  None or \
            not isinstance(value, Citta) or \
                hash(self)!=hash(value):
            return False
        return self._nome == value._nome and self._numAbitanti == value._numAbitanti
   
   
    def set_nome(self,nome:str)->None:
        if not self._nome:
            raise ValueError("Il nome non può essere vuoto")
        else:
            self._nome=nome


    def set_abitanti(self,num:int)->None:
        if self._numAbitanti < 0:
            raise ValueError("Il numero degli abitanti non può essere negativo")
        else:
            self._numAbitanti=num


    def get_nome(self)->str:
        return self._nome
   
    def get_abitanti(self)->int:
        return self._numAbitanti
   
class Nazione:
    _nome:str


    def __init__(self, nome:str):
        self._nome=nome
   
    def __hash__(self)->int:
        return hash((self._nome))
   
    def __eq__(self, value)-> bool:
        if value in  None or \
            not isinstance(value, Nazione) or \
                hash(self)!=hash(value):
            return False
        return self._nome == value._nome
   
   
    def set_nome(self,nome:str)->None:
        if not self._nome:
            raise ValueError("Il nome non può essere vuoto")
        else:
            self._nome=nome
       
    def get_nome(self)->str:
        return self._nome
    
volo1:Volo=Volo(None,360)
aereoporto1:Aereoporto=Aereoporto("Aereoporto di Napoli","AS879")
aereoporto2:Aereoporto=Aereoporto("Aereoporto di Malpensa","MA4544")
compagnia1:Compagnia=Compagnia("Luca&co",2021)
citta1:Citta=Citta("Napoli",123456978)
nazione1:Nazione=Nazione("Europa")

print(f"Il volo numero {volo1._codice} è partito dall'{aereoporto1._nome} e arrivera all'{aereoporto2._nome}. Il volo durerà: {volo1._durata_minuti} minuti")