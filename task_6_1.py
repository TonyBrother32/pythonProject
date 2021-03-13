file_1 = open('log.txt', 'r', encoding='utf-8')
result = []
for line in file_1:
    lst_log = line.replace('-', '').replace('"', '').split(' ')
    lst_request = [lst_log[0], lst_log[5], lst_log[6]]
    result.append(tuple(lst_request))
print(result)
file_1.close()

