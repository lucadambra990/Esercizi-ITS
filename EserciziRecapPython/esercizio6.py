def media(lista:list)->float:
    s=0
    if not lista:
        return None
    for i in lista:
        s=s+i
    m=s/len(lista)
    return m
print(media([1,2,3,4]))