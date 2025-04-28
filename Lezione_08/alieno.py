class Alieno:
    '''
    
    Di un alieno ci interessa sapere la galassia di provenienza
    self.galaxy:str
    
    '''


    # inizializzare un oggetto della classe Alieno
    def __init__(self,galaxy:str):
        self.setGalaxy(galaxy)


    # definire un metdodo per impostare il valore dell'attributo setGalaxy
    def setGalaxy(self, galaxy:str)->None:
        if galaxy:
            self.galaxy=galaxy
        else:
            print("Errore! La galassia non può essere una stringa vuota")

    # definire un metodo per restituire il valore dell'attributo self.galaxy
    def getGalaxy(self)->str:
        return self.galaxy
    
    # definire un metodo speak()
    def speak(self)->None:
        print("jjajajdfjaScottMcTominayuhfjhfsbfusbfu")
    def __str__(self)->str:
        return f"Alieno proveniente dalla galassia {self.getGalaxy()}"