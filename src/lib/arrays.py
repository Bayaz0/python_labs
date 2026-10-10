#минимальный и максимальный элементы из списка
def min_max(nums):
    if not nums:
        raise ValueError("ValueError")
    copy_nums = list(nums)
    min, max = copy_nums[0], copy_nums[0]
    for num in copy_nums:
        if num > max:
            max = num
        if num < min:
            min = num
    return min, max

#сортировка пузырьком (без повторов)
def bubble_sort(nums):
    unique_nums = set(nums)
    copy_nums = list(unique_nums)
    n = len(copy_nums)
    for i in range(n):
        for j in range(n - i - 1):
            if copy_nums[j] > copy_nums[j + 1]:
                copy_nums[j], copy_nums[j + 1] = copy_nums[j + 1], copy_nums[j]
    return copy_nums

#слияние строк/кортежей
def flatten(mat):
    res = []
    for row in mat:
        if type(row) in (list, tuple):
            for num in row:
                res.append(num)
        else:
            raise TypeError("TypeError")
    return res