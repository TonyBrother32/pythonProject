class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def convert_date(cls, date):
        day, month, year = map(int, date.split('-'))
        return f'день {day}, месяц {month}, год {year}'

    @staticmethod
    def validate_date(date):
        day, month, year = map(int, date.split('-'))
        if 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 2999:
            return "Формат даты верен"
        else:
            return "Формат даты не верен"


print(Date.convert_date("25-03-1989"))
print(Date.validate_date("25-13-1989"))
print(Date.validate_date("25-03-1989"))
