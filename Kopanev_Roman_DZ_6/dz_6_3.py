# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении
# данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
# загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в
# словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в
# файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
import json
from itertools import zip_longest
users = []
hobbies = []
with open('files/users.csv', 'r', encoding='utf-8') as f:
    for line in f:
        users.append(line.strip().replace(',', ' '))

with open('files/hobby.csv', 'r', encoding='utf-8') as f:
    for line in f:
        hobbies.append(line.strip())
if len(users) < len(hobbies):
    exit(1)
dict_users = {user: hobby for (user, hobby) in zip_longest(users, hobbies)}

with open('files/dict_users.json', 'w', encoding='utf-8') as f:
    json.dump(dict_users, f)
with open('files/dict_users.json', 'r', encoding='utf-8') as f:
    print(json.load(f))










