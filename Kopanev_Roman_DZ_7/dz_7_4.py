# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера
# файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых не
# превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
my_folder_path = os.path.join(BASE_DIR, 'some_data')


def show_stat(folder_path):
    stat = get_stat(folder_path)
    keys = list(stat)
    keys.sort()
    for key in keys:
        return f'{key}: {stat[key]}'


def get_stat(folder_path):
    stat = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            size = os.stat(os.path.join(root, file)).st_size
            key = 10 ** len(str(size))
            if key in stat:
                stat[key] += 1
            else:
                stat[key] = 1
    if stat == {}:
        raise Exception('Пустая директория')
    print(stat)
    return stat


if __name__ == '__main__':
    try:
        my_folder_path = './'
        show_stat(my_folder_path)
    except Exception as e:
        print(e)
        exit(1)

