class Worker:

    def __init__(self, name, surname, position, i_1, i_2):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": i_1, "bonus": i_2}


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{(int(self._income["wage"]) + int(self._income["bonus"]))}')


clerk = Position("Duke", "Nukem", "Shooter", "10000", "5000")
clerk.get_full_name()
clerk.get_total_income()

driver = Position("Vin", "Dizel", "Driver", "12000", "7000")
driver.get_full_name()
driver.get_total_income()
