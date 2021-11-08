# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
import re


class Data:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'{self.data}'

    @classmethod
    def convert(cls, data):
        instance = cls(cls.validator(data))
        return instance

    @staticmethod
    def validator(data):
        pattern = re.compile(r'(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d+)$')
        result = pattern.match(data)
        if not result:
            raise ValueError('Некорректная дата')
        result = result.groupdict()
        for key in result.keys():
            result[key] = int(result[key])
        if result['day'] < 1 or result['day'] > 31:
            raise ValueError('Некорректное число')
        if result['month'] < 1 or result['month'] > 12:
            raise ValueError('Некорректный месяц')
        if result['year'] < 1 or result['year'] > 5000:
            raise ValueError('Введите год в заданном диапазоне')
        return result


date = Data('05-11-2021')
print(date)
my_date = Data.convert('05-11-2021')
print(my_date)
# print()
# my_date = Data.convert('35-11-2021')
# print(my_date)





