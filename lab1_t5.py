0.
Присвоїти
цілій
змінній
d
першу
цифру
з
дробової
частини
позитивного
дійсного
числа
x.


def drobov_num(a):
    result = int(a * 10) % 10
    return result


b = float(input("Введіть дробове позитивне число: "))
if b > 0:
    print(drobov_num(b))
else:
    print("Введіть дробове позитивне число (a > 0)!")


# 2
