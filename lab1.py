#4. Дано катети прямокутного трикутника a і b. Знайти його гіпотенузу c і
import math


def triangle(side_a, side_b):
    side_c = math.sqrt(side_a ** 2 + side_b ** 2)
    per = side_a + side_b + side_c
    return side_c, per


a = int(input("Введіть сторону a: "))
b = int(input("Введіть сторону b: "))

print("Гіпотенуза і периметр трикутника: ", triangle(a, b))
