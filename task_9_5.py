class Stationery:
    title = "scissors"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Ручка для текста")


class Pencil(Stationery):
    def draw(self):
        print("Карандаш для рисунка")


class Handle(Stationery):
    def draw(self):
        print("Маркер для презентаций")


mapped = Pen()
mapped.draw()
papermate = Pencil()
papermate.draw()
erichkrause = Handle()
erichkrause.draw()
