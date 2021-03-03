list_price = [57.8, 46.51, 97, 88.88, 12.15, 24.3, 91.23, 44.87, 51.89, 19.99, 37.3, 67.08]
list_part = []
for idx in range(len(list_price)):
    price_str = 0
    if type(list_price[idx]) != float:  # проверяем число целое или нет
        list_price[idx] = list_price[idx]/1
    price_str = str(list_price[idx])  # переводим число в строку
    price_str = price_str.split(".")  # делим строку по точке
    if len(price_str[1]) == 1:   # проверяем сколько чисел после точки
        price_str[1] = price_str[1] + "0"
    list_part.append(price_str[0] + " руб " + price_str[1] + " кооп")
print("Список с рублями и копейками ", list_part)
print("Подтверждение что объект списка тот же ", id(list_part))
list_part.sort()
print("Список цен, отсортированный по возрастанию ", list_part)
print("Подтверждение что объект списка тот же ", id(list_part))
list_sorted = sorted(list_part, reverse=True)
print("Новый список по убыванию ", list_sorted)
list_five_position = list(reversed(list_sorted[:5]))
print("Пять самых дорогих товаров по возрастанию ", list_five_position)
