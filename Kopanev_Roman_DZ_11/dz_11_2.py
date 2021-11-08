# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых
# пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class MyZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


def division():
    try:
        num1 = int(input('Введите делимое: '))
        num2 = int(input('Введите делитель: '))
        if num2 == 0:
            raise MyZeroDivision('На ноль делить нельзя')
        else:
            result = num1 / num2
            return result
    except ValueError:
        return 'Введите корректное число'
    except MyZeroDivision as e:
        return e


print(division())
