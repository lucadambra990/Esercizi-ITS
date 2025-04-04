def somma_elementi(x: list[int],y:list[int]) -> list[int]:
    result:list[int] = []
    for i in range(len(x)):
        result.append(x[i] + y[i])
    return result

print(somma_elementi([1,2,3],[4,5,6]))