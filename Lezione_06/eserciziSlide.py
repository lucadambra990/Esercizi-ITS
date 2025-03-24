class Person:
    def __init__(self, name:str,age:int):
        self.name = name
        self.age = age


alice:Person = Person("Alice W.", 45)
bob:Person = Person("Bob M.", 36)
luca:Person = Person("Luca D", 21)
manuel:Person = Person("Manuel N",20)
samuel:Person = Person("Samuel",19)



print(f"L'età di bob è {bob.age}")#1.Stampa l'età tramite la dot notation

if alice.age > bob.age:
    print(f"La persona più vecchia è {alice.name}")#2. if per stampare la persona più vecchia
else:
    print(f"La persona più vecchia è {bob.name}")


#forma compatta
# oldest_name = alice.name if alice.age > bob.age else bob.name
# print(f"{oldest_name} è il più vecchio")


people:list[Person] = [alice,bob,luca,manuel,samuel]#3. lista people riempita con gli oggetti persona   

#4. esegue un controllo sulla lista e stampa il nome del più giovane
person = people[0]# Uso un puntatore per far partire il controllo dal primo elemento
for i in people:
    if i.age < person.age:
        person=i
print(f"Il più giovane è: {person.name}")