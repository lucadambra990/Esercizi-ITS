mydict:dict = {"key1":"value1", "key2":"value2"}

for key in mydict: #ciclo for per iterare il dizionario e restituire in output le chiavi 
    print(key)

for key in mydict: #ciclo for per iterare il dizionario e restituire il output i valorei del dizionario a seconda della chiave associata
    print(mydict[key])

for keys, values in mydict.items():#la funzione items serve a restituire una lista di tuple, ogni tupla e una coppia di elementi chiave - valore
    print(f"chiave:{keys}, valore:{values}")#ciclo for che restituisce  una tupla key-valore grazie alla funzione items

for value in mydict.values():#restituisce una lista con i valori del dizionario
    print(f"il valore del elemento del dizionario è:{value}")

for key in mydict.keys():#restituisce una lista con i valori delle chiavu del dizionario
    print(key)

firstlst:list = [1,2,3,4,5] #tramite questa struttura aggiungiamo in una lista un dizionario
firstlst.extend({"key":"value", "Bool":"True"}.items())#con la funzione items aggiungiamo alla lista delle tuple con gli elementi chiavi-valore del dizionario
print(firstlst)