class posMil:
    def __init__(self,nome:str):
        self._nome:str=""

    def setPos(self, posMil:str):
        self._nome = posMil
        
    def getPos(self):
        return self._nome
