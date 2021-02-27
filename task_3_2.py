num_words = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
             "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate():
    num = input("Введите число на английском ")
    if num[0].isupper():
        print(f"Перевод на русский '{num_words.get(num.lower()).capitalize()}'")
    else:
        print(f"Перевод на русский '{num_words.get(num)}'")


num_translate()
