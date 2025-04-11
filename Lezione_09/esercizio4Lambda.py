names:list[tuple] = [("Luca", 21), ("Anna", 19), ("Marco", 22)]
sorted_by_ages:list[int] = sorted(names, key=lambda ages:tuple[0](ages))
print(sorted_by_ages)