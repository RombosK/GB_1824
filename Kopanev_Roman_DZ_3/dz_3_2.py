# Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(args):
    num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    for i in args:
        if i.isupper():
            return num_dict.get(args.lower()).capitalize()
        else:
            return num_dict.get(args.lower())


print(num_translate_adv('one'))
print(num_translate_adv('One'))
print(num_translate_adv('zero'))
print(num_translate_adv('TEN'))
