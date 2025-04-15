from PersonaErede import Persona
from studente import Studente

# creo un oggetto della classe Persona
p1:Persona = Persona("Luca","D'Ambra",21)

# visualizzare le informazioni relative all'oggetto p1
print(p1)

# creo un oggetto della classe studente
studente1:Studente = Studente("Mario","Rossi",20,"45454545")

# visualizzare le informazioni relative all'oggetto studente1
print(studente1)

# controllo se studente1 sia istanza della classe studente
# isistance(obj, Class) -> controlla se l'oggetto obj sia oggetto della classe "class"
# in caso affermativo -> True
# in caso negativo -> False
if isinstance(studente1, Studente):
    print("\nstudente1 è istanza della classe Studente")

# controllo se studente1 è istanza della classe Persona
if isinstance(studente1, Persona):
    print("\nstudente1 è anche istanza della classe Persona")

# controllare se p1 è istanza della classe Persona
if isinstance(p1, Persona):
    print("\nl'oggetto p1 è istanza della classe Persona")

# controllare se l'oggetto p1 è istnza della claasse Studente
if isinstance(p1, Studente):
    print("\nl'oggetto p1 è istanza della classe Studente")
else:
    print("\nl'oggetto p1 è istanza della classe Persona ma non è istanza della classe Studente")

# controllare che la classe Studente sia sottoclasse della classe Persona
# issubclass(Class1, Class2) -> controlla se Class1 sia sottoclasse di Class2
# in caso affermativo -> True
# in caso negativo -> False
if issubclass(Studente, Persona):
    print("\nla classe Studente è sottoclasse della classe Persona")