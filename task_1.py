"""Задача на практику алгоритмов:
Допустим, мы проводим онлайн-конкурс работ молодых художников. Всего представлено:
N работ, которые идентифицируются числами от 0 до N + 1.

Нужно поддержать 3 типа запроса:
Лайк работы с идентификатором id.
Дизлайк работы с идентификатором id.
Вернуть лучшие K работ. Оценку работы будем считать просто: число лайков минус число дизлайков.
P.S.
Сначала попробовал решить сам, затем изучил решение представленное в Практикуме.
Из-за маленького опыта в ООП, на практике всегда применяю процедурное решение. Хотя в этом примере видимо лучше ООП."""

import random


# Решение от Яндекс.Практикум с использованием ООП
class Competition:
    def _change_score(self, participant_id, change):
        self._scores[participant_id] += change

    def __init__(self, participant_count) -> None:
        self._scores = [0] * participant_count

    def like(self, participant_id) -> None:
        self._change_score(participant_id, 1)

    def dislike(self, participant_id):
        self._change_score(participant_id, -1)

    def get_best_works(self, count):
        scores_ids = [(value, id) for id, value in enumerate(self._scores)]
        scores_ids.sort(reverse=True)
        return [id for _, id in scores_ids[:count]]


# Моё решение без использования ООП
def like(case: any) -> None:
    """Функция принимает id работы, которую надо лайкнуть; ищет по ключу в словаре лайков и увеличивает значение"""
    cases_likes[case] = cases_likes.get(case) + 1


def dislike(case: any) -> None:
    """Функция принимает id работы, которую надо дизлайкнуть; ищет по ключу в словаре дизлайков
     и увеличивает значение"""
    cases_dislikes[case] = cases_dislikes.get(case) + 1


def counter(data_1: dict, data_2: dict) -> dict:
    """Функция возвращает словарь с результатами голосования для каждой работы:
        — Вычитает из количества лайков дизлайки"""
    diff_results = {}
    for key, value in data_2.items():
        diff = data_1[key] - value
        diff_results[key] = diff

    return diff_results


def get_best(data: dict, best: int) -> list:
    """Сортирует по значениям словарь и возвращает нужное количество элементов"""
    top = sorted(data, key=data.get, reverse=True)[:best]
    return top


if __name__ == '__main__':
    N = 11
    # Экземпляр класса, который принимает в себя количество выставленных работ | Практикум
    cases_oop = Competition(participant_count=N)
    # Данные для работы функций отбора | Мое решение
    cases_foo = [i for i in range(N)]
    cases_likes = {item: 0 for item in cases_foo}
    cases_dislikes = {item: 0 for item in cases_foo}
    # Тест
    for i in range(100_000):  # 100_000 членов жюри ставят одному участнику лайк, а одному дизлайк

        # Случайный идентификатор участника, кому поставят лайк
        case_id = random.randrange(0, 11)
        # Метод
        cases_oop.like(case_id)
        # Функция
        item = cases_foo[case_id]
        like(item)

        # Случайный идентификатор участника, кому поставят дизлайк
        case_id = random.randrange(0, 11)
        # Метод
        cases_oop.dislike(case_id)
        # Функция
        item = cases_foo[case_id]
        dislike(item)

    # Результаты ООП
    top_cases_oop = cases_oop.get_best_works(count=5)
    # Результаты функций отбора
    cases_diff = counter(cases_likes, cases_dislikes)
    top_cases_foo = get_best(data=cases_diff, best=5)
    # Вывод на экран
    print(top_cases_oop)
    print(top_cases_foo)
