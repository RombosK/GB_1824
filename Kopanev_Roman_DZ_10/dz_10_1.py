# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать
# данные (список списков) для формирования матрицы. Mатрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Cложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
import random
ROWS = 4
COLS = 4


class Matrix:
    def __init__(self, my_list: list):
        self.my_list = my_list

    def __str__(self):
        print(f'<< MATRIX >>')
        return '\n'.join(map(str, self.my_list))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix.__str__(self)


def dig():
    return [[random.randint(-10, 10) for i in range(COLS)]
        for j in range(ROWS)]


matrix = Matrix(dig())
print(matrix)
other_matrix = Matrix(dig())
print(other_matrix)
print(matrix.__add__(other_matrix))

