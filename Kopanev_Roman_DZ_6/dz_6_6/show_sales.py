

def show_sales(argv):
    program, *args = argv
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        lines = sum(1 for i in f)
        f.seek(0)
        count = 1
        result = {}
        for line in f:
            string = line.strip()
            key = str(count)
            result.setdefault(key, string)
            count += 1
        if len(sys.argv) == 1:
            print(*result.values(), sep="\n")
        elif len(sys.argv) == 2:
            print(args)
            for i in range(int(args[0]), lines + 1):
                print(result[f'{i}'])
        elif len(sys.argv) == 3:
            if int(args[1]) > lines:
                for i in range(int(args[0]), lines + 1):
                    print(result[f'{i}'])
            else:
                for i in range(int(args[0]), int(args[1]) + 1):
                    print(result[f'{i}'])


if __name__ == '__main__':
    import sys
    exit(show_sales(sys.argv))

