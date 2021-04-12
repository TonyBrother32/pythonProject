class DivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


first_digit = input("Введите делимое: ")
second_digit = input("Введите делитель: ")

try:
    first_digit = int(first_digit)
    second_digit = int(second_digit)
    if second_digit == 0:
        raise DivisionError("На ноль делить нельзя")
except ValueError:
    print("Вы ввели не число")
except DivisionError as err:
    print(err)
else:
    print(f"Результат деления: {first_digit / second_digit}")
