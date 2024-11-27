# 1нч 2п 3в 4п
def f(x, y, h):
    if (h == 3 or h == 5) and x + y >= 39:
        return 1
    elif h == 5 and x + y < 39:
        return 0
    elif x + y >= 39 and h < 5:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 1, y, h + 1) and f(x, y + 1, h + 1) and f(x * 2, y, h + 1) and f(x, y * 2, h + 1)  # ход Пети
        else:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)  # ход Вани

def f1(x, y, h):
    if h == 3 and x + y >= 39:
        return 1
    elif h == 3 and x + y < 39:
        return 0
    elif x + y >= 39 and h < 3:
        return 0
    else:
        if h % 2 != 0:
            return f1(x + 1, y, h + 1) and f1(x, y + 1, h + 1) and f1(x * 2, y, h + 1) and f1(x, y * 2, h + 1)  # Ход Пети
        else:
            return f1(x + 1, y, h + 1) or f1(x, y + 1, h + 1) or f1(x * 2, y, h + 1) or f1(x, y * 2, h + 1)  # Ход Вани

for x in range(1, 30):
    if f(x, 9, 1) == 1:
        print(x)
print()
for x in range(1, 30):
    if f1(x, 9, 1) == 1:
        print(x)