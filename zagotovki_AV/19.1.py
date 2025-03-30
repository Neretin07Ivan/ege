def f(x, h):
    # Базовые случаи
    if h == 3 and x >= 108:
        return 1
    elif h == 3 and x < 108:
        return 0
    elif x >= 108 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            # Ход победителя (используем OR)
            if x % 2 == 0:
                return f(x + 1, h + 1) or f(int(x * 1.5), h + 1)
            else:
                return f(x + 1, h + 1) or f(x * 2, h + 1)
        else:
            # Ход проигравшего (используем AND)
            if x % 2 == 0:
                return f(x + 1, h + 1) and f(int(x * 1.5), h + 1)
            else:
                return f(x + 1, h + 1) and f(x * 2, h + 1)

# Перебираем все возможные начальные значения x
for x in range(1, 108):
    if f(x, 1) == 1:
        print(x)