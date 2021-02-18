num = int(input("Введите количество секунд: "))
# print ("Hi, ", name, sep="")
day = num // (3600*24)
h = num // 3600
h = h % 24
m = num // 60
m = m % 60
s = num % 60
print(day, "дней", h, "час", m, "мин", s, "сек")
