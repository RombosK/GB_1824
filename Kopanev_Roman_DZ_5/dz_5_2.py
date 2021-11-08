#Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


def odd_nums(n: int):
    odd_to_n = (num for num in range(1, n + 1, 2))
    #print(type(odd_to_n))
    return odd_to_n


print(*odd_nums(15))
print(*odd_nums(32))
