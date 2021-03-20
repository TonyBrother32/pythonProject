n = int(input("Введите число "))
odd_number = (num for num in range(1, n+1, 2))
print(*odd_number)
