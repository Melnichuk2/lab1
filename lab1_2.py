# 8. Відомо, що X кг цукерок коштують A гривень. Визначити, скільки коштує 1 кг і Y кг цих же
# цукерок.


def money_x(mon_a, mon_b):
    cost_x = mon_b / mon_a
    return cost_x


def money_y(mon_y, mon_x):
    cost_y = mon_y * mon_x
    return cost_y


a = int(input("Введіть х кг цукерок: "))
b = int(input("Скільки вони коштують?: "))
y = int(input("Введіть y кг цукерок: "))
x = money_x(a, b)
print("1 кг коштує: ", money_x(a, b))
print("y кг коштує: ", money_y(y, x))
