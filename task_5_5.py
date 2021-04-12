from time import perf_counter
start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_src = [num for num in src if src.count(num) == 1]
print(result_src, perf_counter() - start)

##################################################################
start = perf_counter()
unique_number = set()
tmp = set()
for num in src:
    if num not in tmp:
        unique_number.add(num)
    else:
        unique_number.discard(num)
    tmp.add(num)
unique_number_src = [num for num in src if num in unique_number]
print(unique_number_src, perf_counter() - start)
