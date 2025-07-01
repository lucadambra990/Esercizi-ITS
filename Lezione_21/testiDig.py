class Documento():
    text:str
    def __init__(self,testo:str):
        self.set_testo(testo)

    def set_testo(self,testo:str):
        self.text = testo

    def getText(self):
        return self.text
    
    def isInText(self,parola:str):
        if parola in self.text:
            return True
        return False
    
class Email(Documento):
    _mittente:str
    _destinatario:str
    _title:str
    def __init__(self, testo, mittente:str,destinatario:str,title:str):
        super().__init__(testo)
        self.setMittente(mittente)
        self.setDest(destinatario)
        self.setTitle(title)

    def setMittente(self,mittente:str):
        self._mittente = mittente

    def setDest(self,dest:str):
        self._destinatario = dest

    def setTitle(self,title:str):
        self._title = title

    def getMittente(self):
        return self._mittente
    
    def getDest(self):
        return self._destinatario
    
    def getTitle(self):
        return self._title
    
    def getText(self):
        return f"Da: {self.getMittente()}, A: {self.getDest()} \n Titolo: {self.getTitle()}\n Messaggio: {super().getText()}"
    
    def writeTofile(self):
        with open('/home/its/Scrivania', 'w') as file:
            file.write(self.getText())
        return file 


class File(Documento):
    nomePercorso:str
    def __init__(self, nomePercorso:str):
        self.nomePercorso = nomePercorso
        super().__init__(self.leggiTestoDaFile())
        


    def leggiTestoDaFile(self):
        with open(self.nomePercorso, 'r') as file:
           contenuto = file.readlines()
        return contenuto

    def getText(self):
        return f"Percorso: {self.nomePercorso}\n Contenuto: {super().getText()}"


file1:File = File('/home/its/document.txt')
print(file1.leggiTestoDaFile())

