class Pagamento():
    _importo:float
    def __init__(self):
        self.setImporto(0.00) # questo quando non si vuole passare tramite input un parametro

    def setImporto(self,imp:float):
        self._importo=imp

    def getImporto(self):
        return self._importo
    
    def dettagliPagamento(self):
        return f"L'importo del pagamento è {self._importo:.2f}"