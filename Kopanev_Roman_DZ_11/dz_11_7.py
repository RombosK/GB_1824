# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку методов
# сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
# выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного результата.
class ComplexNumbers:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.res = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма x1 и x2 равна')
        """Формула расчёта суммы комплексных чисел"""
        return f'res = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение x1 и x2 равно')
        """Формула расчёта произведения комплексных чисел"""
        return f'res = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'res = {self.a} + {self.b} * i'


x_1 = ComplexNumbers(1, 2)
x_2 = ComplexNumbers(3, 4)
print(x_1)
print(x_2)
print(x_1 + x_2)
print(x_1 * x_2)

