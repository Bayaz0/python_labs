"""
python -m src.lab07.check — прогоняет всё и печатает OK:
N проверок или падает на первом расхождении
"""
import random
from src.lib.sorting import bubble_sort, insertion_sort, selection_sort
from src.lib.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def check_sorting(fn, trials=100) -> None:
    """
    случайные списки длиной от 0 до 50, значения от −100 до 100, с повторами
    assert fn(nums) == sorted(nums)
    плюс assert nums == копия — исходный не изменён
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"

def check_search() -> None:
    """
    на случайных списках linear_search против list.index (и -1 против ValueError)
    binary_search — на отсортированных, включая x, которого нет, и крайние элементы
    """
    #линейная сортировка
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-100, 100)
        result = linear_search(nums, x)
        try:
            index_excpected = nums.index(x)
        except ValueError:
            index_excpected = -1
        
        assert result == index_excpected, f"{linear_search.__name__} ошиблась на {nums} : {result}, поиск x = {x}"

    #бинарная сортировка
    flag = random.randint(5, 10)
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        sorted_nums = sorted(nums)

        #краевые случаи
        if flag and sorted_nums:
            x = random.choice([sorted_nums[0], sorted_nums[-1], random.random()])
            flag -= 1
        else:
            x = random.randint(-100, 100)

        result = binary_search(sorted_nums, x)

        try:
            index_excpected = sorted_nums.index(x)
        except ValueError:
            index_excpected = -1

        if x not in sorted_nums:
            assert result == index_excpected, f"{binary_search.__name__} ошиблась на {sorted_nums} : {result} для элемента {x} находящегося вне списка"
        else:
            assert sorted_nums[result] == sorted_nums[index_excpected], f"{binary_search.__name__} ошиблась на {sorted_nums} : {result}, поиск x = {x}, правильный индекс {index_excpected}"

def check_two_sum(trials=100) -> None:
    """ оба способа должны давать пару с нужной суммой или оба None"""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-100, 100)

        result_brute = two_sum_brute(nums, x)
        result_fast = two_sum_fast(nums, x)

        if result_brute == None or result_fast == None:
            assert result_brute == result_fast, (
                f"На списке {nums} функция two_sum_brute вернула {result_brute};"
                                                 f"функция two_sum_fast вернет {result_fast} при поиске элемента {x}")
        else:
             assert nums[result_brute[0]] + nums[result_brute[1]] == nums[result_fast[0]] + nums[result_fast[1]] == x, (
                f"На списке {nums} функция two_sum_brute вернула {nums[result_brute[0]]} + {nums[result_brute[1]]};"
                                                 f"функция two_sum_fast вернет {nums[result_fast[0]]} + {nums[result_fast[1]]} при поиске элемента {x}")
           
if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, selection_sort, insertion_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()

    print("OK")