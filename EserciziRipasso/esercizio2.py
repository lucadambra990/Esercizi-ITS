from typing import Any
def listaDict(lista:list[int|float])->dict:
    dict1:dict[Any,Any]={}
    lista_neg:list=[]
    lista_pos:list=[]
    for i in lista:
        if i < 0:
            lista_neg.append(i)
            dict1["negativi"]=lista_neg
        else:
            lista_pos.append(i)
            dict1["positivi"]=lista_pos
    return dict1
print(listaDict([1,2,5,9,8,7,6,-6,-5,-7,-4,-5,0])) 