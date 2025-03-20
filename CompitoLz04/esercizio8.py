#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato
#in una lista di numeri interi. 
#Un elemento è considerato isolato 
#se non è affiancato sia a destra che a sinistra da elementi uguali.





def count_isolated(lista:list) -> int:
    count=0
    for i in range(len(lista)):
        if i==0 and lista[0]!=lista[1]: 
            count+=1
        else:
            i==1 and lista[i]!=lista[i+1] or lista[i-1]
            count+=1
    return count

print(count_isolated([1, 1, 2, 2, 3, 4, 4]))