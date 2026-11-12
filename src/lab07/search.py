def linear_search(nums, x) -> int:
    """индекс первого вхождения, иначе -1"""
    n = len(nums)
    for i in range(n):
        if x == nums[i]:
            return i
    return -1

def binary_search(sorted_nums, x) -> int:
    """
    индекс любого вхождения, иначе -1; цикл while lo <= hi;    
    на неотсортированном списке результат не определён
    """
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        i = (lo + hi) // 2
        mid = sorted_nums[i]
        if mid == x:
            return i
        elif mid < x:
            lo = i + 1
        else:
            hi = i - 1
    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """пара индексов (i, j), i < j, или None"""
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (nums[i] + nums[j]) == target:
                return (i, j)
    return None

def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """
    то же через словарь за один проход;
    при нескольких ответах допустим любой
    """
    n = len(nums)
    d = dict()
    for i, num in enumerate(nums):
        addition = target - num
        if addition in d:
            return (d[addition], i)
        d[num] = i    
    return None

if __name__ == "__main__":
    print(linear_search([4, 2, 7, 2], 2))
    print(binary_search([1, 3, 5, 7], 4))
    print(two_sum_fast([1, 2], 10))
    print(two_sum_brute([2, 7, 11, 15], 9))