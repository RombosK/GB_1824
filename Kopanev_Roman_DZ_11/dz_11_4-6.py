# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
class Warehouse:
    def __init__(self, brand: str, cost: int, quantity: int, num_of_lists: int, *args):
        self.brand = brand
        self.cost = cost
        self.quantity = quantity
        self.num = num_of_lists
        self.main_shop = []
        self.shop = []
        self.unit = {'Модель': self.brand, 'Цена за шт.': self.cost, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.brand} цена {self.cost} количество {self.quantity}'

    def data(self):
        try:
            unit_b = input('Введите название: ')
            unit_c = int(input('Введите цену: '))
            unit_q = int(input('Введите количество: '))
            result = {'Модель': unit_b, 'Цена за шт.': unit_c, 'Колчество': unit_q}
            self.unit.update(result)
            self.shop.append(self.unit)
            print(f'Готовый список: -\n {self.shop}')
        except:
            return f'Ошибка ввода'

        print(f'Для завершения нажмите - Q, для продолжения - Enter')
        q = input(f'Нажмите >>>')
        if q == 'Q' or q == 'q':
            self.main_shop.append(self.shop)
            print(f'Основной склад -\n {self.main_shop}')
            return f'Выход'
        else:
            return Warehouse.data(self)


class Printer(Warehouse):
    def print(self):
        return f'Текст на печать {self.num} раз(-а)'


class Scanner(Warehouse):
    def scans(self):
        return f'Сканировать текст {self.num} раз(-а)'


class Xerox(Warehouse):
    def copier(self):
        return f'Копировать текст {self.num} раз(-а)'


unit_1 = Printer('HP', 12000, 5, 10)
unit_2 = Scanner('Canon', 14000, 5, 10)
unit_3 = Xerox('Xerox', 7500, 1, 15)
print(unit_1.data())
print(unit_2.data())
print(unit_3.data())
print(unit_1.print())
print(unit_2.scans())
print(unit_3.copier())





