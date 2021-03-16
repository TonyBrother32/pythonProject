result = []
with open('log.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        lst_log = line.replace('-', '').replace('"', '').split(' ')
        lst_request = [lst_log[0], lst_log[5], lst_log[6]]
        result.append(tuple(lst_request))
    print(result)

dict_ip = {}
list_hack = [x[0] for x in result]
count, itm = 0, 0
for item in list_hack:
    dict_ip[item] = dict_ip.get(item, 0) + 1
    if dict_ip[item] >= count:
        count, itm = dict_ip[item], item
print(f'Количество запросов {count} ip адрес хакера {itm}')





