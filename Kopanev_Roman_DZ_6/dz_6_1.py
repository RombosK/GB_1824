#  Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида:
#  (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.


def parse_log(log):
    temp_log = log.split(' ')
    return tuple([temp_log[0], temp_log[5].replace('"', ''), temp_log[6]])


log_lst = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    log = f.readline()
    while log:
        log_lst.append(parse_log(log))
        log = f.readline()

print(log_lst)

