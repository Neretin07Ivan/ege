def f(n):
    s = ""
    while n > 0:
        s += str(n % 7)
        n //= 7
    if len(s) > 0:
        return int(s[::-1])
    else:
        return 0

k = 0
for i in range(0, 10 ** 10):
    n = str(f(i))
    if len(str(n)) == 6:
        if n.count("0") == 1:
            s = 0
            for j in n:
                if int(j) % 2 == 0 and j != "0":
                    s += 1
            if s % 2 == 0:
                k += 1
    else:
        if len(n) > 6:
            break
print(k)
