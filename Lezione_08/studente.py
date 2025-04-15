# importare dal modulo persona.py la classe Persona
from PersonaErede import Persona

class Studente(Persona):
    '''
    Attributi della classe persona (in quanto studente eredita da Persona)
    self.name: str
    self.lastname: str
    self.age: int

    Attributi della classe Studente
    self.matricola: str
    '''

    #inizializzare un oggetto della classe Studente
    def __init__(self, name:str, lastname:str, age:int, matricola:str):

        #inizializzare la classe Persona richiamando il metood init della superclasse
        super().__init__(name, lastname, age)

        # istruzioni che inizializzano uno oggetto della classe Studente
        self.setMatricola(matricola)

        # metodi setter
        
        # metodo che imposta il valore del setMatricola
    def setMatricola(self,matricola:str) ->None:
        if matricola:
            self.matricola = matricola
        else:
            print("Errore! La matricola non può essere rappresentata da una stringa vuota")
        
        # metodo getter

        #metodo che ritorna il valore dell'attributo self.matricola
    def getMatricola(self)->str:
        return self.matricola
    
    # ridefinire il metodo str
    def __str__(self)->str:
        return f"\nNome: {self.name} \nCognome: {self.lastname}\nMatricola: {self.matricola}"