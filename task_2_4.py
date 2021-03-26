list_position = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for part in list_position:
    list_part = part.split(" ")
    name = list_part.pop()
    print(f"Привет, {name.capitalize()} !")
