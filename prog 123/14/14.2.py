def f4(n):
    k3 = 0
    while n > 0:
        if n%4 == 3:
            k3 += 1
        n = n//4
    return k3

n = 16**18*4**10-4**6-16
print(f4(n))
