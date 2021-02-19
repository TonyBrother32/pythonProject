number = 0
odd_number = []
while number < 1000:
    if not number % 2:
        number += 1
    else:
        odd_number.append(number**3)
        number += 1
print("Список чисел ", odd_number)
total_sum = 0  # сумма чисел, сумма цифр которых кратна 7
sum_digit = 0  # сумма цифр числа
for digit in odd_number:
    total_sum_digit = 0
    last_digit = 0
    sum_digit = digit
    while digit > 0:
        last_digit = digit % 10  # определяем последнюю цифру
        digit = digit // 10  # перезаписываем число без последней цифры
        total_sum_digit += last_digit  # суммируем все цифры числа
    if (total_sum_digit % 7) == 0:    # если сумма всех чисел числа делится на 7 без остатка, то число нам подходит
        total_sum += sum_digit
print("Сумма чисел, сумма цифр которых кратна 7, ", total_sum)
for idx in range(len(odd_number)):
    odd_number[idx] += 17  # увеличиваем каждое число списка на 17
print("Список чисел, увеличенный на 17 ", odd_number)
total_sum = 0
sum_digit = 0
for digit in odd_number:
    total_sum_digit = 0
    last_digit = 0
    sum_digit = digit
    while digit > 0:
        last_digit = digit % 10  # определяем последнюю цифру
        digit = digit // 10  # перезаписываем число без последней цифры
        total_sum_digit += last_digit  # суммируем все цифры числа
    if (total_sum_digit % 7) == 0:    # если сумма всех чисел числа делится на 7 без остатка, то число нам подходит
        total_sum += sum_digit
print("Сумма чисел, сумма цифр которых кратна 7, ", total_sum)
