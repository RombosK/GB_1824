# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
class Road:
    _length: int
    _width: int

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def mass(self):
        m_square = 25
        thickness = 5
        x = self._length * self._width * m_square * thickness
        res = f'{x/1000} т'
        return res


road = Road(5000, 20)
print(road.mass())
road = Road(3000, 20)
print(road.mass())
