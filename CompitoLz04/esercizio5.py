from typing import Any
def remove_duplicates(lista:list) -> list:
    results:list[Any] = []
    for i in lista:
        if i not in results:
            results.append(i)
    return results

print(remove_duplicates([1,1,2,3,4,"a","a",3,5,5,7,9]))