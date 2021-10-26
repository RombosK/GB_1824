# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os
from os import path, mkdir

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def starter(dir_path, dir_name, folders):
    current_path = path.join(dir_path, dir_name)
    if not path.exists(current_path):
        mkdir(current_path)
    for folder in folders:
        current_folder = path.join(current_path, folder)
        if not path.exists(current_folder):
            mkdir(current_folder)


if __name__ == '__main__':
    my_name = 'my_project'
    my_path = './'
    my_folders = ('settings', 'mainapp', 'adminapp', 'authapp')
    try:
        starter(my_path, my_name, my_folders)

    except Exception as e:
        print(e)
