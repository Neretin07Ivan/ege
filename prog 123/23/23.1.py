
def F(x, n):
    if x == n:
        return 1
    if x == 25:
        return 0
    if x > n:
        return 0

    return F(x + 3, n) + F(x * 2, n) + F(x * 5, n)


print(F(5, 115))