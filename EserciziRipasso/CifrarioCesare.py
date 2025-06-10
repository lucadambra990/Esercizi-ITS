from string import ascii_lowercase,ascii_uppercase

def caesar_cypher_encrypt(s:str, key:int)->str:
    risultato:str=""
    for i in s:
        if i in ascii_lowercase:
            new_index=(ascii_lowercase.index(i) + key)%len(ascii_lowercase)
            risultato+=ascii_lowercase[new_index]
        elif i in ascii_uppercase:
            new_index=(ascii_uppercase.index(i) + key)%len(ascii_uppercase)
            risultato+=ascii_uppercase[new_index]
        else:
            raise ValueError("Il valore di i non è un lettera dell'alfabeto")
    return risultato





def caesar_cypher_decrypt(s:str, key:int)->str:
    risultato:str=""
    for i in s:
        if i in ascii_lowercase:
            new_index=(ascii_lowercase.index(i) + key)%len(ascii_lowercase)
            risultato+=ascii_lowercase[new_index]
        elif i in ascii_uppercase:
            new_index=(ascii_uppercase.index(i) + key)%len(ascii_uppercase)
            risultato+=ascii_uppercase[new_index]
        else:
            raise ValueError("Il valore di i non è un lettera dell'alfabeto")
    return risultato



print(caesar_cypher_encrypt("a",28))
print(caesar_cypher_encrypt("CIAO",6))
print(caesar_cypher_decrypt("gtyretdg",-2))
print(caesar_cypher_decrypt("TRGDEHG",-8))

# fkqecpg