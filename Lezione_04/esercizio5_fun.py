def add_one(a:int):
    result = a+1
    return result
def add_one_to_list(lista:list[int]):
    new_list:list[int] = []
    for i in lista:
        new_list.append(add_one(i))
    return new_list

lista:list[int] = [1,2,3]
new_list=add_one_to_list(lista)
print(new_list)



