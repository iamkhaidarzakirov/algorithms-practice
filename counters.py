

def count_chars(s: str) -> dict:
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1
    return counter


def recount_chars_count(data: dict) -> dict:
    recounter = {}
    for key, value in data.items():
        recounter[value] = recounter.get(value, []) + [key]
    return recounter


if __name__ == '__main__':
    string = 'zfmsdzlgndjkgdagad;gadgldsghldgdfkgadkfgagadlkgndaklgakgtjej'
    print(count_chars(string))
    print(recount_chars_count(count_chars(string)))
