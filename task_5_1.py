def odd_number_generator(n):
    for num in range(1, n+1, 2):
        yield num


odd_number = odd_number_generator(55)
print(*odd_number)
