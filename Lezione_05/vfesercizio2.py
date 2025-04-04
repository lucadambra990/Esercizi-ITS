def even_odd_pattern(numbers:list[int]) -> list[int]:
    pari:list[int] = []
    dispari:list[int] = []
    for i in numbers:
        if i%2==0:
            pari.append(i)
        elif i%2==1:
            dispari.append(i)
    return pari + dispari

print(even_odd_pattern([1,5,6,8,4,3]))