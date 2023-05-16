"""Написать функцию сортировки элементов списка | Сортировка выбором. Сложность O(n^2)"""


def sort_arr(arr: list[int]) -> list[int]:
    """По умолчанию, сортирует элементы списка по возрастанию."""

    for i in range(len(arr)):
        # В любом случае сравнение начинается с первого элемента
        current_el = arr[i]
        current_el_index = i
        for j in range(i + 1, len(arr)):
            # Переопределяем минимальный элемент и его индекс
            if current_el > arr[j]:
                current_el = arr[j]
                current_el_index = j
        arr.insert(i, arr.pop(current_el_index))
    return arr


if __name__ == '__main__':
    nums = [16, 32, 0, 1, 4, 3, 67, 54, 33, 21, 68, 78, 87, 55]
    print(sort_arr(arr=nums))
