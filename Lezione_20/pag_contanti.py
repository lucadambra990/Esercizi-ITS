from typing import Any
from gest_pag import *

class PagamentoContanti(Pagamento):
    def __init__(self,importo:float):
        self.setImporto(importo)

    def inPezziDa(self):
        soldi:list[Any] = [500,200,100,50,20,10,5,2,1,0.50,0.20,0.10,0.05,0.01]
        for i in soldi:
            volte=int(self._importo//i)
            resto=round(self._importo%i,2)
            self._importo=resto
            if volte > 0:
                print(f"{volte} banconota da {i}")
    
if __name__ == "__main__":
    payment:PagamentoContanti = PagamentoContanti(1500.00)
    print(payment.dettagliPagamento())
    payment.inPezziDa()