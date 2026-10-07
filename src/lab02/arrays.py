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

def test_min_max():
    print(min_max([3, -1, 5, 5, 0]))
    print(min_max([42]))
    print(min_max([-5, -2, -9]))
    try:
        print(min_max(list()))
    except ValueError as e:
        print(e)
    print(min_max([1.5, 2, 2.0,-3.1]))

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

def test_bubble_sort():
    print(bubble_sort([3, 1, 2, 1, 3]))
    print(bubble_sort(list()))
    print(bubble_sort([-1, -1, 0, 2, 2]))
    print(bubble_sort([1.0, 1, 2.5, 2.5, 0]))

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

def test_flatten():
    print(flatten([[1, 2], [3, 4]]))
    print(flatten([[1, 2], (3, 4, 5)]))
    print(flatten([[1], list(), [2, 3]]))
    try:
        print(flatten([[1, 2], "ab"]))
    except TypeError as e:
        print(e)
   
#test_min_max()
#test_bubble_sort()
test_flatten()
