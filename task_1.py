duration = int(input("Введите количество секунд:  "))
second_limit = 60
minute_limit = 3600
hour_limit = 24
day_limit = 30
month_limit = 12
day = duration // (minute_limit*hour_limit)
day = day % day_limit
hour = duration // minute_limit
hour = hour % hour_limit
minute = duration // second_limit
minute = minute % second_limit
second = duration % second_limit
month = duration // (minute_limit*hour_limit*day_limit)
month = month % month_limit
year = duration // (minute_limit*hour_limit*day_limit*month_limit)
print(year, 'лет', month, "мес", day, "дн", hour, "час", minute, "мин", second, "сек")
