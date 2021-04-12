from abc import abstractmethod


class Store:
    def __init__(self):
        self.dict = {}

    def add_to_store(self, equipment):
        self.dict.setdefault(equipment, []).append(equipment)


class OfficeEquipment:
    def __init__(self, name, serial_number, is_colour):
        self.name = name
        self.serial_number = serial_number
        self.colour = is_colour

    def __str__(self):
        return f'{self.name} {self.serial_number} {self.colour}'

    @property
    @abstractmethod
    def action(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, name, serial_number, is_colour, printer_type):
        super().__init__(name, serial_number, is_colour)
        self.printer_type = printer_type

    def __str__(self):
        return f'{self.name} {self.serial_number} {self.colour} {self.printer_type}'

    @property
    def action(self):
        return 'Принтер печатает'


class Scaner(OfficeEquipment):
    def __init__(self, name, serial_number, is_colour, a_format):
        super().__init__(name, serial_number, is_colour)
        self.format = a_format

    def __str__(self):
        return f'{self.name} {self.serial_number} {self.colour} {self.format}'

    @property
    def action(self):
        return 'Сканер сканирует'


class Xerox(OfficeEquipment):
    def __init__(self, name, serial_number, is_colour, copy_speed):
        super().__init__(name, serial_number, is_colour)
        self.copy_speed = copy_speed

    def __str__(self):
        return f'{self.name} {self.serial_number} {self.colour} {self.copy_speed}'

    @property
    def action(self):
        return 'Копир копирует'


store_office = Store()
scaner_1 = Scaner("hp", "584768", True, "A4")
scaner_2 = Scaner("canon", "5823423424", True, "A3")
store_office.add_to_store(scaner_1)
store_office.add_to_store(scaner_2)
printer_1 = Printer('samsung', "3453453", None, "Лазерный")
store_office.add_to_store(printer_1)
print(*store_office.dict)

