# 1нч 2п 3в 4п
def f(x,y,h):
    r = (x**2 + y**2)**0.5
    if (h == 3 or h == 5) and r > 14:
        return 1
    if h == 5 and r < 14:
        return 0
    if h < 5 and r > 14:
        return 0
    if h % 2 == 0:
        return f(x * 2, y, h + 1) or f(x, y + 3, h + 1) or f(x, y + 4, h + 1)
    else:
        return f(x * 2, y, h + 1) and f(x, y + 3, h + 1) and f(x, y + 4, h + 1)

for x in range(1, 14):
    if f(3, x, 1) == 1:
        print(x)

print()
# 1нч 2п 3в 4п
def f(x,y,h):
    r = (x**2 + y**2)**0.5
    if (h == 3) and r > 14:
        return 1
    if h == 3 and r < 14:
        return 0
    if h < 3 and r > 14:
        return 0
    if h % 2 == 0:
        return f(x * 2, y, h + 1) or f(x, y + 3, h + 1) or f(x, y + 4, h + 1)
    else:
        return f(x * 2, y, h + 1) and f(x, y + 3, h + 1) and f(x, y + 4, h + 1)

for x in range(1, 14):
    if f(3, x, 1) == 1:
        print(x)