class Persona:
    '''
    Di una persona dobbiamo sapere delle informazioni.
    Queste informazioni vengono chiamate attributi (della classe Persona)
    Le informazioni saranno:
    - nome
    - cognome
    - età

    come li rappresento in python?

    self.name:str (attributo di tipo stringa)
    self.name:str (attributo di tipo stringa)
    self.age:int (attributo di tipo intero)

    '''


    # costruttore della classe Persona
    # il costrutture serve a creare una variabile del tipo della classe (in questo caso Persona)
    # SELF indica che init è una funzione della classe (in questo caso Persona)
    def __init__(self,name:str,lastname:str, age:int):
        self.name = name
        self.lastname = lastname
        self.age = age

    # funzione che mostri in output tutti i dati di una persona
    def displayData(self) -> None:
        print(f"Nome:{self.name}\nCognome:{self.lastname}\nEtà:{self.age}")


l:Persona = Persona("Luca","D'Ambra",21)# in questo modo istanziamo una variabile di tipo persona
print(l)  # in questo modo restituisce la posizione del dato in memoria
# mostra i dati di una persona
l.displayData()
