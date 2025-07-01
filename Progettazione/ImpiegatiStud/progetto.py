class Progetto:
    _nome:str
    def __init__(self,nome:str):
        self.setNome(nome)

    def setNome(self,nome:str):
        self._nome = nome

    def getNome(self):
        return self._nome