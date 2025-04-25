# 1нч 2п 3в 4п 5в
def f(n,k):
    if (k == 3 or k == 5) and (n > 96 and n < 106):
        return True
    if (k == 2 or k == 4) and n > 105:
        return True
    if k == 5 and (n < 97 or n > 105):
        return False
    if n > 96 and n < 106 and k < 5:
        return False
    if k % 2 == 0:
        return f(n + 3, k + 1) or f(n + 5, k + 1) or f(n * 3, k + 1)
    else:
        return f(n + 3, k + 1) and f(n + 5, k + 1) and f(n * 3, k + 1)
k = 0
for S in range(1, 97):
    if f(S, 1):
        k += 1
        print(S)

print()
def f(n,k):
    if (k == 3) and (n > 96 and n < 106):
        return True
    if (k == 2) and n > 105:
        return True
    if (n > 96 and n < 106) and k < 3:
        return False
    if k == 3 and (n < 97 or n > 105):
        return False
    if k % 2 == 0:
        return f(n + 3, k + 1) or f(n + 5, k + 1) or f(n * 3, k + 1)
    else:
        return f(n + 3, k + 1) and f(n + 5, k + 1) and f(n * 3, k + 1)

for S in range(1, 97):
    if f(S, 1):
        k -= 1
        print(S)
print()
print(k, "k")