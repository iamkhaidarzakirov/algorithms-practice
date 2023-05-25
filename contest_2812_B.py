def test():
    # Данные для вывода рассортированы по словарям
    side_indexes = {'left': 0, 'right': 1}
    position_indexes = {'aisle': {0: 2, 1: 0}, 'window': {0: 0, 1: 2}}
    seats_naming = {0: {0: 'A', 1: 'B', 2: 'C'}, 1: {0: 'D', 1: 'E', 2: 'F'}}
    # Переменная состояния
    is_ok = None
    for wish in wishes:  # Перебираем пожелания пассажиров
        p_count = int(wish[0])  # Количество пассажиров
        side = side_indexes[wish[1]]  # Желаемая сторона самолета
        pos_ind = position_indexes[wish[2]][side]  # Индекс желаемого места
        for row in orig_scheme:  # Перебираем ряды
            is_ok = True  # Оптимистичный настрой
            places = list(row[side])  # 3 сиденья
            free = places.count('.')  # Сколько из них свободны
            # Дальше перебираем все возможные условия
            if p_count == 3 and free == 3:
                orig_scheme[orig_scheme.index(row)][side] = 'XXX'
                if side == 0:
                    print(
                        f'Passengers can take seats: {orig_scheme.index(row) + 1}A {orig_scheme.index(row) + 1}B {orig_scheme.index(row) + 1}C')
                    for item in orig_scheme:
                        print('_'.join(item))
                        orig_scheme[orig_scheme.index(item)][side] = orig_scheme[orig_scheme.index(item)][side].replace(
                            'X', '#')
                else:
                    print(
                        f'Passengers can take seats: {orig_scheme.index(row) + 1}D {orig_scheme.index(row) + 1}E {orig_scheme.index(row) + 1}F')
                    for item in orig_scheme:
                        print('_'.join(item))
                        orig_scheme[orig_scheme.index(item)][side] = orig_scheme[orig_scheme.index(item)][side].replace(
                            'X', '#')
                break
            elif p_count == 1 and free >= 1 and places[pos_ind] == '.':
                places[pos_ind] = 'X'
                orig_scheme[orig_scheme.index(row)][side] = ''.join(places)
                print(f'Passengers can take seats: {orig_scheme.index(row) + 1}{seats_naming[side][pos_ind]}')
                for item in orig_scheme:
                    print('_'.join(item))
                    orig_scheme[orig_scheme.index(item)][side] = orig_scheme[orig_scheme.index(item)][side].replace(
                        'X', '#')
                break
            elif p_count == 2 and free >= 2 and places[1] != '#' and places[pos_ind] == '.':
                if side == 0 and pos_ind == 2:
                    places[pos_ind] = 'X'
                    places[pos_ind - 1] = 'X'
                    orig_scheme[orig_scheme.index(row)][side] = ''.join(places)
                    print(
                        f'Passengers can take seats: {orig_scheme.index(row) + 1}{seats_naming[side][pos_ind - 1]} {orig_scheme.index(row) + 1}{seats_naming[side][pos_ind]}')
                    for item in orig_scheme:
                        print('_'.join(item))
                        orig_scheme[orig_scheme.index(item)][side] = orig_scheme[orig_scheme.index(item)][side].replace(
                            'X', '#')
                    break
                elif side == 0 and pos_ind == 0:
                    places[pos_ind] = 'X'
                    places[pos_ind + 1] = 'X'
                    orig_scheme[orig_scheme.index(row)][side] = ''.join(places)
                    print(
                        f'Passengers can take seats: {orig_scheme.index(row) + 1}{seats_naming[side][pos_ind]} {orig_scheme.index(row) + 1}{seats_naming[side][pos_ind + 1]}')
                    for item in orig_scheme:
                        print('_'.join(item))
                        orig_scheme[orig_scheme.index(item)][side] = orig_scheme[orig_scheme.index(item)][side].replace(
                            'X', '#')
                    break
                elif side == 1 and pos_ind == 0:
                    places[pos_ind] = 'X'
                    places[pos_ind + 1] = 'X'
                    orig_scheme[orig_scheme.index(row)][side] = ''.join(places)
                    print(
                        f'Passengers can take seats: {orig_scheme.index(row) + 1}{seats_naming[side][pos_ind]} {orig_scheme.index(row) + 1}{seats_naming[side][pos_ind + 1]}')
                    for item in orig_scheme:
                        print('_'.join(item))
                        orig_scheme[orig_scheme.index(item)][side] = orig_scheme[orig_scheme.index(item)][side].replace(
                            'X', '#')
                    break
                else:
                    places[pos_ind] = 'X'
                    places[pos_ind - 1] = 'X'
                    orig_scheme[orig_scheme.index(row)][side] = ''.join(places)
                    print(
                        f'Passengers can take seats: {orig_scheme.index(row) + 1}{seats_naming[side][pos_ind - 1]} {orig_scheme.index(row) + 1}{seats_naming[side][pos_ind]}')
                    for item in orig_scheme:
                        print('_'.join(item))
                        orig_scheme[orig_scheme.index(item)][side] = orig_scheme[orig_scheme.index(item)][side].replace(
                            'X', '#')
                    break
            else:
                is_ok = False
        if not is_ok:
            print('Cannot fulfill passengers requirements')


if __name__ == '__main__':
    # Ввод в терминал
    istyping = False
    if istyping:
        n = int(input())
        orig_scheme = [input().split('_') for i in range(n)]
        m = int(input())
        wishes = [input().split() for i in range(m)]

    else:  # Для тестов в среде лучше использовать чтение из файла
        with open('data/requirements.txt', 'r', encoding='utf-8') as text:
            requirements = text.read().split('\n')
        # Parse text
        n = int(requirements[0])
        del requirements[0]
        orig_scheme = [item.split('_') for item in requirements[:n]]
        del requirements[:n]
        m = requirements[0]
        del requirements[0]
        wishes = [item.split() for item in requirements[:]]

    # Print requirements / Помогает во время тестирования
    isprint = False
    if isprint:
        print(*wishes, sep='\n')
        print(*orig_scheme, sep='\n')
    test()
