"""Дана строка в кодировке utf-8. Нужно найти самый часто встречающийся символ в строке и вывести сообщение
по шаблону: Символ <символ> встречается <количество> раз """


class Solution:
    def __init__(self, string: str) -> None:
        self.string = string

    def count_chars(self) -> dict:
        """Считает количество уникальных символов в строке, путем добавления символа в качестве ключа словаря,
        и при каждом совпадении увеличивает значение по ключу на 1"""
        chars_counter = {}
        for char in self.string:
            chars_counter[char] = chars_counter.get(char, 0) + 1
        return chars_counter


if __name__ == '__main__':
    s = input('Введите строку для анализа: ')
    solution = Solution(string=s)
    count_dict = solution.count_chars()
    frequent = sorted(count_dict, key=count_dict.get, reverse=True)[0]
    print(f'Символ {frequent} встречается {count_dict[frequent]} раз(а)')

