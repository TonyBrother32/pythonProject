def odd_number_generator(n):
    for num in range(1, n+1, 2):
        yield num


print(*odd_number_generator(55))
