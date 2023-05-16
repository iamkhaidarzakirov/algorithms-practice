"""[Грокаем алгоритмы] Алгоритм быстрой сортировки / Рекурсия"""

import random


def qs(arr: list[int]) -> list[int]:
    """Рекурсивная функция быстрой сортировки.
    Базовым случаем является массив из одного элемента. Такой массив не требует сортировки.
    Во всех других случаях определяется стартовая точка и два массива, с числами меньше и больше стартовой.
    Эти массивы передаются обратно в функцию, пока не будет достигнут базовый случай."""
    if len(arr) < 2:
        return arr
    else:
        start_point = arr[len(arr) // 2]  # Лучший сценарий со стартовой точкой в центре массива
        less = [item for item in arr if item < start_point]
        great = [item for item in arr if item > start_point]
        return qs(less) + [start_point] + qs(great)


if __name__ == '__main__':
    random_int_list = []
    for i in range(1, 26):
        r = random.randrange(1, 50)
        if r not in random_int_list:
            random_int_list.append(r)

    print(random_int_list)
    print(qs(random_int_list))
