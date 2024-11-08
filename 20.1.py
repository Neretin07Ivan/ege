
# нн1 п2 в3 п4
def f(x, h):
    if h == 4 and x >= 108:
        return 1
    elif h == 4 and x < 108:
        return 0
    elif x >= 108 and h < 4:
        return 0
    else:
        if h % 2 == 0:
            if x % 2 ==0:
                return f(x + 1, h + 1) and f(x * 1.5, h + 1)  # стратегия победителя
            else:
                return f(x + 1, h + 1)  and f(x * 2, h + 1)   # стратегия победителя
        else:
            if x % 2 == 0:
                return f(x + 1, h + 1) or f(x * 1.5, h + 1)  # стратегия проигравшего(неудачный ход)
            else:
                return f(x + 1, h + 1) or f(x * 2, h + 1)  # стратегия проигравшего(неудачный ход)

for x in range(1, 108):
    if f(x, 1) == 1:
        print(x)