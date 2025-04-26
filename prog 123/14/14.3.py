def f5(n):
    k4 = 0
    while n > 0:
        if n%5 == 4:
            k4 += 1
        n = n//5
    return k4

n = 5**36+5**24-25
print(f5(n))