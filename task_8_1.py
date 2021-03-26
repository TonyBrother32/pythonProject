import re


def mail_is_valid(name):
    RE_NAME = re.search(r'([\w.-]+)@([\w.-]+\.[a-zA-Z])', name)
    if RE_NAME:
        dict_mail = {"name_user": RE_NAME.group(1), "domain": RE_NAME.group(2)}
        print(dict_mail)
    else:
        raise ValueError


try:
    mail_is_valid(input("Введите e-mail для проверки "))
except ValueError:
    print("Неверный e-mail")
