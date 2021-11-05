# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
# существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
# Проверить работу этих методов на реальных данных.Выполнить общий подсчёт расхода ткани. Проверить на практике полученные
# на этом уроке знания. Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    count = 0

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    def __init__(self, name: str, size: float):
        super().__init__(name)
        self.size = size

    @property
    def calculate(self):
        result = self.size / 6.5 + 0.5
        Clothes.count += round(result, 1)
        return f'Для пальто нужно {result:.2f} м. ткани'


class Suit(Clothes):
    def __init__(self, name: str, height: float):
        super().__init__(name)
        self.height = height

    @property
    def calculate(self):
        result = 2 * self.height + 0.3
        Clothes.count += round(result, 1)
        return f'Для костюма нужно {result:.2f} м. ткани'


coat = Coat('Пальто', 32)
print(coat.calculate)
suit = Suit('Костюм', 1.83)
print(suit.calculate)
print(Clothes.count)

