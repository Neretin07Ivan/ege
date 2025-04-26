def f3(n):
    k2 = 0
    while n > 0:
        if n%3 == 2:
            k2 += 1
        n = n//3
    return k2

n = 9**11*3**20-3**9-27
print(f3(n))