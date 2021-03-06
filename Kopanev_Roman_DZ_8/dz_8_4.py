# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
# исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
def val_checker(check_func):
    def decor(func):
        def wrapper(*args):
            if not check_func(*args):
                raise ValueError(f'wrong val: {args[0]}')
            res = func(*args)
            return res
        return wrapper
    return decor


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    print(calc_cube(5))
    print(calc_cube(-5))
except ValueError as e:
    print(e)
