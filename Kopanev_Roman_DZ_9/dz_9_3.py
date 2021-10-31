# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname} - доход за месяц:'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


w1 = Position('Александр', 'Петров', 'Junior Python Developer', 65000, 7500)
print(w1.get_full_name(), w1.get_total_income())
w2 = Position('Василий', 'Ложкин', 'Middle Python Developer', 110000, 12000)
print(w2.get_full_name(), w2.get_total_income())
w3 = Position('Марк', 'Сахоров', 'Senior Python Developer', 180000, 20000)
print(w3.get_full_name(), w3.get_total_income())
