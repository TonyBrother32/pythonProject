class Cell:

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if self.count - other.count > 0:
            return self.count - other.count
        else:
            print("Разность клеток меньше ноля")

    def __mul__(self, other):
        return self.count * other.count

    def __floordiv__(self, other):
        return self.count // other.count

    def make_order(self, rows):
        return "\n".join(["*" * rows for _ in range(self.count // rows)]) + "\n" + "*" * (self.count % rows)


cell_1 = Cell(23)
cell_2 = Cell(19)

print(f'Объединение двух клеток {cell_1 + cell_2}')
print(f'Вычитание клеток {cell_1 - cell_2}')
print(f'Умножение клеток {cell_1 * cell_2}')
print(f'Деление клеток {cell_1 // cell_2}')
print(f'Вывод по рядам \n{cell_1.make_order(4)}')
