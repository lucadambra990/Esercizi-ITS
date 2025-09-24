from gest_pag import *

class PagamentoCartaDiCredito(Pagamento):
    _nomeTitolare:str
    _dataScad:str
    _numCarta:int
    def __init__(self,importo:float,nomeTitolare:str,data_scad:str,num_carta:int):
        self.setImporto(importo)
        self.setNomeTitolare(nomeTitolare)
        self.setDataScad(data_scad)
        self.SetNumCarta(num_carta)

    def setNomeTitolare(self,nome:str):
        self._nomeTitolare=nome

    def setDataScad(self,data:str):
        self._dataScad=data

    def SetNumCarta(self,num_carta:int):
        self._numCarta=num_carta

    def getNomeTitolare(self):
        return self._nomeTitolare
    
    def getDataScad(self):
        return self._dataScad
    
    def getNumeroCarta(self):
        return self._numCarta
    
    
if __name__ == "__main__":
    cardPay:PagamentoCartaDiCredito=PagamentoCartaDiCredito(2500.00,"Luca D'Ambra","12/28",6545656489448298)
    print(cardPay.dettagliPagamento())
    print(cardPay.getNomeTitolare())
    print(cardPay.getDataScad())
    print(cardPay.getNumeroCarta())