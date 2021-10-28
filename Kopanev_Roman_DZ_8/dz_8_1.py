#  Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
#  и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном
#  случае использовать функцию re.compile()?
from re import findall


def email_parse(email_address):
    temp = r'(^[a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$)'
    result = findall(temp, email_address)
    if len(result) == 0:
        raise ValueError(f'wrong email: {email_address}')
    return {'username': result[0][0], 'domain': result[0][1]}


email_address = 'teacher@geekbrains.com'
try:
    print(email_parse(email_address))
except ValueError as e:
    print(e)
finally:
    print('End')
email_address = 'teacher$geekbrains.ru'
try:
    print(email_parse(email_address))
except ValueError as e:
    print(e)
finally:
    print('End')

