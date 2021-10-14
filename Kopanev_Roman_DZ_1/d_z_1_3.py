# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого
# из чисел в интервале от 1 до 100:
a = 'процентов'
b = 'процента'
c = 'процент'
for number in range(1, 101):
    if 10 < number < 15:
        print(number, a)
    elif (number % 10) == 1 and number != 11:
        print(number, c)
    elif (number % 10) == 2 and number != 12:
        print(number, b)
    elif (number % 10) == 3 and number != 13:
        print(number, b)
    elif (number % 10) == 4 and number != 14:
        print(number, b)
    else:
        print(number, a)
