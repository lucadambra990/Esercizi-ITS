def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return sum(numbers) / len(numbers)
    else:
        return sum(numbers)/len(numbers)

print(calculate_average([2,6,9,8,7]))