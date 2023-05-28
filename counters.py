from typing import Sequence


def count_chars(s: Sequence) -> dict:
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1
    return counter


def recount_chars_count(data: dict) -> dict:
    """Функция группирует символы с одинаковым количеством вхождений в строке"""
    recounter = {}
    for key, value in data.items():
        recounter[value] = recounter.get(value, []) + [key]
    return recounter


if __name__ == '__main__':
    string = 'zfmsdzlgndjkgdagad;gadgldsghldgdfkgadkfgagadlkgndaklgakgtjej'
    string_list = list(string)
    print(count_chars(string_list))
    print(recount_chars_count(count_chars(string)))
