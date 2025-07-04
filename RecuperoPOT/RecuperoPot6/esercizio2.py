lista_nomi:list[str] = []
while len(lista_nomi)<=30:
    name = str(input("Inserisci dei nomi: "))
    if not name or len(name) > 20:
        print("Il nome che inserisci non può essere una stringa vuota o non deve superare i 20 caratteri")
    if name in lista_nomi:
        print("Il nome inserito è già presente nella lista")
        break
    lista_nomi.append(name)

maxs = max(lista_nomi,key=len)
print(f"Hai inserito {len(lista_nomi)} nomi distinti")
print(f"Il nome più lungo è {maxs} con {len(maxs)}")
