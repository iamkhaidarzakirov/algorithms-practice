
def sort_dict(music: dict) -> dict:
    """Функция возвращает отсортированный словарь.
    При помощи dictionary comprehension формируется отсортированный словарь, итерируясь по отсортированному
    по убыванию списку ключей принятого словаря с исполнителями и их количеством воспроизведений"""
    sorted_music = {artist: music[artist] for artist in sorted(music, key=music.get, reverse=True)}

    return sorted_music


if __name__ == '__main__':
    # Input
    with open('data/artists.txt', 'r', encoding='utf-8') as file:
        """list comprehensions создает список кортежей по 2 str() элемента и преобразует строку с количеством 
        воспроизведений в int(), чтобы в функции при сортировке по значениям словаря, сравнивались числа , 
        а не строки"""
        artists_list = [
            tuple(int(i) if i.isdigit() else str(i) for i in item.split(': ')) for item in file.read().split('\n')
        ]
        # Почему-то вылетает подсказка несоответствия типов, хотя передан итерируемый объект с tuple() из 2 элементов
        music_dict = dict(artists_list)  # ??? Unexpected types ???

    # Output
    for key, value in sort_dict(music_dict).items():
        print(f'{key}: {value}')
