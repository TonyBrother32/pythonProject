class Date:

    def __init__(self, date_as_string):
        self.date_as_string = date_as_string

    @classmethod
    def convert_date(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return f'день {day}, месяц {month}, год {year}'

    @staticmethod
    def validate_date(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 2999:
            return "Формат даты верен"
        else:
            return "Формат даты не верен"


print(Date.convert_date("25-03-1989"))
print(Date.validate_date("25-13-1989"))
print(Date.validate_date("25-03-1989"))
