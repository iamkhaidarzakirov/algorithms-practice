"""Алгоритм Евклида / Нахождение НОД"""


def euclid_alg(sides: str) -> int:
    s = [int(i) for i in sides.split()]
    a = max(s)
    b = min(s)
    while True:
        if a % b == 0:
            return b
        else:
            int_count = a // b
            rest = a - (b * int_count)
            a, b = max(rest, b), min(rest, b)


if __name__ == '__main__':
    print(euclid_alg(sides=input()))
