def cifratura(s:str) -> int:
    for i in s:
        c = ord(i) # la funzione ord, dato un carattere restituisce il valore intero del carattere (tabella ASCII)
        print(f"il valore originale della stringa: {i}")
        print(f"Il valore con lo xor 57 applicato: {c ^ 57}")
        print(f"Il carattere originale è {chr(c^57 ^ 57)}") # la funzione chr, dato valore intero, restituisce il carattere associato a quel valore
cifratura("Nel mezzo del cammin di nostra vita")