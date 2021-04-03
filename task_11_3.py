class DateList(Exception):
    def __init__(self, txt):
        self.txt = txt


list_number = []
date = ""
while not date == "q":
    try:
        date = input("Введите числа, для выхода введите q ")
        if date.isdigit():
            list_number.append(date)
        else:
            raise DateList("Вы ввели не число")
    except DateList as err:
        print(err)
print(f"Вы нажали выход. Введенные числа: {list_number} ")
