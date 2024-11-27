# 1нч 2п 3в 4п
def f(x, y, h):
    if h == 3 and x + y >= 39:
        return 1
    elif h == 3 and x + y < 39:
        return 0
    elif x + y >= 39 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)   # стратегия победителя
        else:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)  # стратегия проигравшего(неудачный ход)

for x in range(1, 30):
    if f(x, 9, 1) == 1:
        print(x)
        break