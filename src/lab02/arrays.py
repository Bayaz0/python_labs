def min_max(nums):
    copy_nums = list(nums)
    if not copy_nums:
        raise ValueError("Список пуст")
    min, max = copy_nums[0], copy_nums[0]
    for num in copy_nums:
        if num > max:
            max = num
        if num < min:
            min = num
    return min, max

ls = []
print(f"{min_max(ls)}")