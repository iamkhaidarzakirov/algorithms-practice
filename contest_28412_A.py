"""Задача А из тренировочного контеста Яндекса"""


def count_operations(arr: list[int]) -> None:
    counter = 0
    if arr != sorted(arr):
        print(-1)
    elif len(arr) == 0:
        print(0)
    else:
        k = arr.index(max(arr))
        diff = max(arr) - arr[0]
        counter += diff
        print(counter)


if __name__ == '__main__':
    n = int(input('Количество резервуаров: '))  # Ненужный параметр
    data = [int(i) for i in input('Литраж резервуаров через пробел: ').split()]
    count_operations(arr=data)
