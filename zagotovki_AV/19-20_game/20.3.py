# 1нч 2п 3в 4п
def f(n,k):
    if k == 4 and 106 > n > 96:
        return 1
    if k == 4 and (n >105 or n < 97):
        return 0
    if k == 3 and n > 105:
        return 1
    if k < 4 and n > 96:
        return 0

    if k % 2 != 0:
        return f(n + 3, k + 1) or f(n + 5, k + 1) or f(n * 3, k + 1)
    else:
        return f(n + 3, k + 1) and f(n + 5, k + 1) and f(n * 3, k + 1)

for S in range(1, 97):
    if f(S, 1):
        print(S)

