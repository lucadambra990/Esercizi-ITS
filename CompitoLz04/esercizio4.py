def rounded_average(numbers: list[int]) -> int:
    s=0
    for i in numbers:
        s=s+i
        m=s/i
    return round(m)
print(rounded_average([2,4,6,5,8]))
