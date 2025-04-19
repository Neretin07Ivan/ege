# 1нч 2п 3в 4п
def f(x, y, h):
    if h == 4 and x + y >= 39:
        return 1
    elif h == 4 and x + y < 39:
        return 0
    elif x + y >= 39 and h < 4:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)  # ход Пети

        else:
            return f(x + 1, y, h + 1) and f(x, y + 1, h + 1) and f(x * 2, y, h + 1) and f(x, y * 2, h + 1)  # ход Вани (любой ход)


for x in range(1, 30):
    if f(x, 9, 1) == 1:
        print(x)


def can_win(a, b, moves):
    # Базовые случаи:
    if a + b >= 180:
        return moves % 2 == 1  # Если текущий игрок сделал победный ход

    # Если превышено максимальное количество ходов (3 хода: Петя-Ваня-Петя)
    if moves >= 3:
        return False

    # Возможные ходы
    options = [
        (a + 2, b),
        (a, b + 2),
        (a + b, b),
        (a, a + b)
    ]

    if moves % 2 == 1:  # Ход Вани (любой его ход должен привести к победе Пети)
        # Все варианты Вани должны позволять Пете выиграть на следующем ходу
        return all(can_win(new_a, new_b, moves + 1) for new_a, new_b in options)
    else:  # Ход Пети (достаточно одного выигрышного варианта)
        # Петя выбирает ход, который гарантирует победу
        return any(can_win(new_a, new_b, moves + 1) for new_a, new_b in options)


# Находим все S, где:
# 1) Петя не может выиграть за 1 ход (sum < 180 после любого его хода)
# 2) Петя может выиграть за 2 хода (после любого хода Вани)
valid_S = []

for S in range(1, 162):
    # Проверяем, что Петя не может выиграть за 1 ход
    petya_first_moves = [
        (18 + 2, S),
        (18, S + 2),
        (18 + S, S),
        (18, 18 + S)
    ]
    if any(a + b >= 180 for a, b in petya_first_moves):
        continue  # Петя может выиграть сразу - не подходит

    # Проверяем, что у Пети есть выигрышная стратегия за 2 хода
    if can_win(18, S, 0):
        valid_S.append(S)

print("Минимальное S:", min(valid_S))
print("Количество возможных S:", len(valid_S))
print("Все подходящие S:", valid_S)