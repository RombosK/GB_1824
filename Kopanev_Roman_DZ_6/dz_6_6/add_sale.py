# Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом командной строки:
# для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
def add_sale(argv: int):
    program, *args = argv
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        for i in range(len(args)):
            f.write(f'{args[i]}\n')


if __name__ == '__main__':
    import sys
    exit(add_sale(sys.argv))


