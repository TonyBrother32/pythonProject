list_names = ("Миша", "Игорь", "Инна", "Марина", "Максим", "Алексей", "Андрей", "Сергей", "Юля")
dict_names = {}


def thesaurus(names):
    for name in names:
        list_for_key = []
        for item in names:
            if item[0] == name[0]:
                list_for_key.append(item)
        dict_names[name[0]] = list_for_key
    print(dict_names)


thesaurus(list_names)