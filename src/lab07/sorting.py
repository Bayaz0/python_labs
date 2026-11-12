def bubble_sort(nums) -> list:
    """
    возвращает новый отсортированный список
    исходный список не меняется
    пустой список и список из одного элемента — работают
    """
    copy_nums = list(nums)
    n = len(copy_nums)
    if n < 2:
        return copy_nums

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if copy_nums[j] > copy_nums[j + 1]:
                copy_nums[j], copy_nums[j + 1] = copy_nums[j + 1], copy_nums[j]
    
    return copy_nums

def insertion_sort(nums) -> list:
    """
    возвращают новый отсортированный список
    исходный список не меняется
    пустой список и список из одного элемента — работают
    """
    copy_nums = list(nums)
    n = len(copy_nums)
    if n < 2:
        return copy_nums

    for i in range(1, n):
        t = i
        for j in range(i - 1, -1, -1):
            if copy_nums[t] >= copy_nums[j]:
                break
            else:
                copy_nums[j], copy_nums[t] = copy_nums[t], copy_nums[j]
                t -= 1

    return copy_nums

def selection_sort(nums) -> list:
    """
    возвращают новый отсортированный список
    исходный список не меняется
    пустой список и список из одного элемента — работают
    """
    copy_nums = list(nums)
    n = len(copy_nums)
    if n < 2:
        return copy_nums

    for i in range(n - 1):
        temp = copy_nums[i]
        jmin = i

        for j in range(i + 1, n):
            if copy_nums[j] < temp:
                temp = copy_nums[j]
                jmin = j

        if jmin != i:
            copy_nums[i], copy_nums[jmin] = temp, copy_nums[i]

    return copy_nums


if __name__ == "__main__":
    print(bubble_sort([3, 7, 1, 12, 4, 6]))
    print(selection_sort([3, 7, 1, 12, 4, 6]))
    print(insertion_sort([3, 7, 1, 12, 4, 6]))