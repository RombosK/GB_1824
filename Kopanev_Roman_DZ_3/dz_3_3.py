#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?

def thesaurus(*names):
    dict_list = {}
    for name in names:
        key = name[0].title()
        if key not in dict_list:
            dict_list[key] = []
        dict_list[key].append(name)
    return dict_list


print(thesaurus("Иван", "Мария", "Петр", "Илья"))





