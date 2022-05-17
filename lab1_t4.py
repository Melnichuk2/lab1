# 16. Визначити число, яке отримано записом у зворотньому
# порядку цифр заданого тризначного числа.


def number_p(a):
    num1 = a // 100
    num2 = (a // 10) % 10
    num3 = a % 10
    three_hun = num3 * 100 + num2 * 10 + num1 * 1
    return three_hun


n = int(input("Введіть n: "))

print(number_p(n))
