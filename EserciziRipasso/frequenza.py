from string import punctuation


def frequenza(lista:list[str])->dict[str,int]:
    dictwords={}
    for i in lista:
        i.lower()
        st=i.strip(punctuation).split(' ')
        for s in st:
            if s in dictwords:
                dictwords[s]+=1
            else:
                dictwords[s]=1
    return dictwords


print(frequenza(["ciao!","cane","ciao-","cane_"]))