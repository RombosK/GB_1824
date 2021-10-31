#  Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title='Ручка'):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует  тонкую линию')


class Pencil(Stationery):
    def __init__(self, title='Карандаш'):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует среднюю линию')


class Handle(Stationery):
    def __init__(self, title='Маркер'):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует толстую линию')


stationery = Stationery('Канцелярская принадлежность для студента')
stationery.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
