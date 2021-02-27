from random import choices
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(w1, w2, w3, numbers=int(input("Сколько хотите шуток? "))):
    """Generate random n jokes"""
    while numbers > 0:
        print(f'{choices(w1)}{choices(w2)}{choices(w3)}'.replace("'", " ").replace("[", "").replace("]", ""))
        numbers -= 1


get_jokes(nouns, adverbs, adjectives)



