"""
одни и те же случайные данные для всех алгоритмов, random.seed(42)
сортировки: n = 1_000, 10_000, 100_000; квадратичные на 10⁵ — ограничить (> 60 с в таблице допустимо)
поиск: список из 100 000, 10 000 случайных запросов; для бинарного — включить время сортировки отдельной строкой
Two Sum: n = 1_000, 10_000, target гарантированно существует
таблица в консоль с выравниванием (f-строки из Л1) и data/lab07/bench.csv через write_csv
"""

import timeit
import random
from src.lib.sorting import bubble_sort, insertion_sort, selection_sort
from src.lib.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lib.io_txt_csv import write_csv

def bench_sorts() -> list[tuple]:
    """три свои сортировки против sorted на n = 1 000 / 10 000 / 100 000"""
    rows = list()
    for n in (1_000, 5_000, 10_000):
        nums = [random.randint(-100, 100) for _ in range(n)]
        for fn in (bubble_sort, insertion_sort, selection_sort):       
            time = timeit.timeit(lambda: fn(nums), number=10)
            rows.append(("sort", n, fn.__name__, round(time / 10, 3)))
    return rows

def bench_searh() -> list[tuple]:
    """линейный против бинарного поиска: 10 000 запросов к списку из 100 000; Возвращает """
    rows = list()
    n = 100_000
    nums = [random.randint(-100_000, 100_000) for _ in range(n)]
    time = timeit.timeit(lambda: sorted(nums), number=10)
    rows.append(("sort", n, sorted.__name__ , round(time / 10, 3)))
    sorted_nums = sorted(nums)

    time = timeit.timeit(lambda: binary_search(sorted_nums, x=random.randint(-100_000, 100_000)), number=10_000) 
    rows.append(("search", 100_000, binary_search.__name__, time ))

    time = timeit.timeit(lambda: linear_search(nums, x=random.randint(-100_000, 100_000)), number=10_000) 
    rows.append(("search", 100_000, linear_search.__name__, time ))

    return rows

def bench_sum() -> list[tuple]:
    """two_sum_brute против two_sum_fast на n = 1 000 / 10 000"""
    rows = list()
    nums1 = [random.randint(-100_000, 100_000) for _ in range(1_000)]
    nums2 = [random.randint(-100_000, 100_000) for _ in range(100_000)]

    for nums in (nums1, nums2):
        for fn in (two_sum_brute, two_sum_fast):
            time = timeit.timeit(lambda: two_sum_brute(nums, target=nums[random.randint(0, 999)] + nums[random.randint(0, 999)]), number=100)
            rows.append(("two_sum", len(nums), fn.__name__, time / 100))
    return rows
    


if __name__ == "__main__":
    header = ("task", "n", "impl", "seconds")
    random.seed(42)
    path = "data/lab07/bench.csv"
    result = bench_sorts() + bench_searh() + bench_sum()
    write_csv(result, path, header=header)

    print(f"{header[0]:<8} | {header[1]:<7} | {header[2]:<15} | {header[3]:<10}")
    print("-" * 50)
    for row in result:
        print(f"{row[0]:<8} | {row[1]:<7} | {row[2]:<15} | {row[3]:<10}")

