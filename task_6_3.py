from json import dump
from itertools import zip_longest

list_users = []
list_hobby = []

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        for line in users:
            list_users.append(line.replace(",", " ").replace("\n", ""))
        for line in hobby:
            list_hobby.append(line.replace(",", " ").replace("\n", ""))
if len(list_users) > len(list_hobby):
    with open('dict_users.json', 'w', encoding='utf-8') as f:
        dict_users = zip_longest(list_users, list_hobby, fillvalue=None)
        result = {el[0]: str(el[1]) for el in dict_users}
        dump(result, f, ensure_ascii=False)
        print(dict_users)
else:
    exit(1)

