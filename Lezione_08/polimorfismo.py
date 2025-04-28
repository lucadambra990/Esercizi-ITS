# il polimorfismo è quando in due classi diverse abbiamo un metodo con lo stesso nome ma che fa cose diverse
from personaPolimorfismo import Persona
from alieno import Alieno

p:Persona=Persona("Luca","D'Ambra",22)

#visualizzare le informazioni dell'oggetto p della classe Persona
print(p)

# creare un oggetto et della classe Alieno
et:Alieno=Alieno("BombardiroCrocodilo")

# visualizzare le informazioni dell'oggetto et
print("\n",et)

# invocare il metodo speak() della classe Persona
p.speak()
print("\n")
# invocare il metodo speak() di un alieno
et.speak()