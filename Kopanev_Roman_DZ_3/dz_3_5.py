# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import *


def get_jokes(n: int, repeat=True):
    """The function creates some jokes"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []

    if repeat is True:
        for _ in range(n):
            jokes_list.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    else:
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for num in range(n):
            if num + 1 > len(nouns) and num + 1 > len(adverbs) and num + 1 > len(adjectives):
                break
            jokes_list.append(f'{nouns[num]} {adverbs[num]} {adjectives[num]}')
    return jokes_list


print(get_jokes(7, repeat=True))
print(get_jokes(7, repeat=False)) # Max 5 Jokes
