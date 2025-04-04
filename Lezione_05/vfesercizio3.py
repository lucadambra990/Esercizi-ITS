def find_disappeared_numbers(nums: list[int]) -> list[int]:
    invisible_num:list[int] = []
    for i in range(1,len(nums)+1):
        if i not in nums:
            invisible_num.append(i)
    return invisible_num

print(find_disappeared_numbers([1,2,3,6,9]))

