from requests import get, utils


def currency_rates(val_item):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    if 2 < len(val_item) < 4 and int(content.find(val_item.upper())) > 0:
        index_date = content.find("Date=")
        date = content[index_date + 6: index_date + 16]
        index = int(content.find(val_item.upper()))
        str_value = content[index: index + 100].replace('>', '').replace('</', '').replace(',', '.').split('Value')
        course = float(str_value[1])
        print(f'Курс {val_item.upper()} на дату {date} по отношению к рублю равен {course}')
    else:
        print("None")


if __name__ == '__main__':
    currency_rates(input("Введите код валюты "))
