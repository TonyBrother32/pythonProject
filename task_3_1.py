num_words = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
             "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate():
    num = input("Введите число на английском ")
    print(f"Перевод на русский '{num_words.get(num)}'four")


num_translate()
