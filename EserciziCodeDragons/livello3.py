def dedup_stable(nums: list[int]) -> list[int]:
    if not nums:  # se la lista è vuota, restituisci subito []
        return []

    new_list = [nums[0]]  # aggiungiamo il primo elemento sempre

    for elem in nums[1:]:  # scorriamo dal secondo elemento in poi
        if elem != new_list[-1]:  # confrontiamo con l'ultimo aggiunto
            new_list.append(elem)

    return new_list




print(dedup_stable([1,1,1,2,3,4,4,5,6]))

