result = []
with open('log.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        lst_log = line.replace('-', '').replace('"', '').split(' ')
        lst_request = [lst_log[0], lst_log[5], lst_log[6]]
        result.append(tuple(lst_request))
    print(result)


