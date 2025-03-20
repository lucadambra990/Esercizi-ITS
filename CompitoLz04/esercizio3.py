def sum_above_threshold(numbers: list[int],threshold) -> int:
    s=0
    for i in numbers:
        if i>threshold:
            s=s+i
    return s
print(sum_above_threshold([15,6,1],16))