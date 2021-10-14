# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.
# a
my_list = []
for x in range(1, 1001, 2):
    my_list.append(x ** 3)
# print(my_list)
num_sum = 0
for i, number in enumerate(my_list):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    if digit_sum % 7 == 0:
        num_sum += my_list[i]
print(num_sum)
# b
num_sum = 0
for i, number in enumerate(my_list):
    digit_sum = 0
    num = number + 17
    while num > 0:
        digit_sum += num % 10
        num //= 10
    if digit_sum % 7 == 0:
        num_sum += my_list[i] + 17
print(num_sum)