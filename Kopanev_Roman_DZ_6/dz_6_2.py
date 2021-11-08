# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.


def parse_log(log):
    temp_log = log.split(' ')
    return tuple([temp_log[0]])


def spamer(logs):
    dict_ip = {}
    count, ip = 0, ''
    for item in log_lst:
        dict_ip[item] = dict_ip.get(item, 0) + 1
        if dict_ip[item] >= count:
            count, ip = dict_ip[item], item
    return tuple([ip[0], count])


log_lst = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    log = f.readline()
    while log:
        log_lst.append(parse_log(log))
        log = f.readline()

print(spamer(log_lst))


