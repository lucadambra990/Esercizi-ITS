from typing import Any
def convertTuple(lista:list[tuple])->dict:
    dict_1:dict[Any,Any]={}
    for element in lista:
        key,value=element[0],element[1]
        if key in dict_1:
            dict_1[key]+=value
        else:
            dict_1[key]=value
    return dict_1

print(convertTuple([("Luca",21),("Giovanni",22),("Matteo",21),(8,"Cani"),(8,"Polli")]))
