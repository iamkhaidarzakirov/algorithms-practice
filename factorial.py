"""[Factorial]
Пример применения:
Строка длиной n имеет n! вариаций перестановок символов;

Формула: n! = 1 * 2 * ...n

Рекуррентная формула:
При n = (0, 1) -> 1;
n! = n * (n - 1)!"""


def factoria1(n: int) -> int:
    """Функция вычисляет факториал числа n, используя цикл"""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def factoria1_r(n: int) -> int:
    """Функция вычисляет факториал числа n, используя рекурсию"""
    if n in (0, 1):
        return 1
    return n * factoria1_r(n - 1)


if __name__ == '__main__':
    num = 100
    print(factoria1(num))
    print(factoria1_r(num))  # Не работает с числом более 995

