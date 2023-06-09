# algorithms-practice
Буду публиковать свои решения некоторых интересных задач, с которыми буду сталкиваться. 

## [Адитья Бхаргава — Грокаем Алгоритмы] Функция реализации алгоритма бинарного поиска.
Файл: binary_search.py

Принцип работы бинарного поиска простыми словами:
Есть искомое число в отсортированном массиве. Берется число из массива с индексом середины и сравнивается с искомым. Если есть совпадение, возвращается индекс этого числа. Ели нет, из поиска убирается
часть массива (значения элементов, которой больше / меньше искомого числа) и поиск продолжается. В худшем случае возвращается None.

## Тренировка *list and dict comprehension* на задаче по сортировке исполнителей.
Файл: comprehensions.py

Есть список музыкальных исполнителей и количество воспроизведений для каждого исполнителя. Этот список передается в виде текстового документа **artists.txt**, где каждый исполнитель на новой строке.
Нужно прочитать файл и отсортировать исполнителей от большего числа воспроизведений к меньшему. После сортировки вывести каждого исполнителя на новой строке.

## Подсчет символов в строке или элементов массива
Файл: counters.py

Реализуйте функцию, которые будут способны подсчитать сколько раз встречается каждый символ в строке или элемент в массиве.

## Тренировочный контест Яндекса

### Андрей и кислота | Задача А.
Файл: contest28412_A.py

- Ограничение времени **2** секунды
- Ограничение памяти 512Mb
- Ввод	стандартный ввод или input.txt
- Вывод	стандартный вывод или output.txt

Андрей работает в секретной химической лаборатории, в которой производят опасную кислоту с удивительными свойствами. У Андрея есть <strong>n</strong> бесконечно больших резервуаров, расположенных в один ряд.
Изначально в каждом резервуаре находится некоторое количество кислоты. Начальство Андрея требует, чтобы во всех резервуарах содержался одинаковый объем кислоты. К сожалению, разливающий аппарат несовершенен.
За одну операцию он способен разлить по одному литру кислоты в каждый из первых **k** резервуаров. Обратите внимание, что для разных операций **k** могут быть разными <strong>(1 <= k <= n)</strong>.
Поскольку кислота очень дорогая, Андрею не разрешается выливать кислоту из резервуаров. Андрей просит вас узнать, можно ли уравнять объемы кислоты в резервуарах.
Если это возможно, то посчитать минимальное количество операций, которое потребуется, чтобы этого достичь.
#### Формат ввода:
- Первая строка содержит число **n** **(от 1 до 100_000)** — количество резервуаров.
- Во второй строке содержатся **n** целых чисел **(от 1 до 10^9)** — содержание кислоты в литрах на данный момент
#### Формат вывода
- Если объемы кислоты в резервуарах можно уравнять, выведите минимальное количество операций, необходимых для этого.
- Если это невозможно, выведите **«-1»**.


### Посадка в самолет | Задача B.
Файл: contest28412_B.py

- Ограничение времени	2 секунды
- Ограничение памяти	512Mb
- Ввод	стандартный ввод или input.txt
- Вывод	стандартный вывод или output.txt

В самолете **n** рядов и по три кресла слева и справа в каждом ряду. Крайние кресла (A и F) находятся у окна, центральные (C и D) – у прохода. 
На регистрацию приходят группы из одного, двух или трех пассажиров. Они желают сидеть рядом, то есть на одном ряду и на одной стороне: левой или правой. 
Например, группа из двух пассажиров может сесть на кресла B и C, но не может сесть на кресла C и D, потому что они разделены проходом, а также не может сесть на кресла A и C, 
потому что тогда они окажутся не рядом. Кроме того, один из пассажиров каждой группы очень требовательный – он хочет сесть либо у окна, либо у прохода. 
Конечно же, каждая группа из пассажиров хочет занять места в ряду с как можно меньшим номером, ведь тогда они скорее выйдут из самолета после посадки. 
Для каждой группы пассажиров определите, есть ли места в самолете, подходящие для них.

#### Формат ввода
Первая строка содержит число **n (1 ≤ n ≤ 100)** – количество рядов в самолете. Далее в n строках вводится изначальная рассадка в самолете по рядам **(от первого до n-го)**, 
где символами . (точка) обозначены свободные места, символами # (решетка) обозначены занятые места, а символами _ (нижнее подчеркивание) обозначен проход между креслами **C и D** каждого ряда.
Следующая строка содержит число **m (1 ≤ m ≤ 100)** – количество групп пассажиров. Далее в **m** строках содержатся описания групп пассажиров. Формат описания такой: 
**num side position**, где num – количество пассажиров (число 1, 2 или 3), side – желаемая сторона самолета **(строка left или right)**, position – желаемое место требовательного пассажира **(строка aisle или window)**.

#### Формат вывода
Если группа может сесть на места, удовлетворяющие ее требованиям, то выведите строку **Passengers can take seats: и список их мест в формате row letter, упорядоченный по возрастанию буквы места**. 
Затем выведите в n строках получившуюся рассадку в самолете, в формате, описанном выше, причем места, занятые текущей группой пассажиров, должны быть обозначены символом **X**.
Если группа не может найти места, удовлетворяющие ее требованиям, то выведите строку **Cannot fulfill passengers requirements***.
Ответ сравнивается с правильным посимвольно, поэтому ваше решение не должно выводить никаких лишних символов, в том числе лишних переводов строк или пробельных символов в концах строк. 
В конце каждой строки (включая последнюю) должен быть выведен символ перевода строки.
  
