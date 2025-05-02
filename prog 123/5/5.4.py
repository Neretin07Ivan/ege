def f3(n):
    s = []
    while n > 0:
        s.append(str(n % 3))
        n = n // 3
    return "".join(s[::-1])

for N in range(1,1000):
    n = f3(N)
    s = ""
    if N % 3 == 0:
        for i in n:
            s += i
            s += i
    else:
        n.replace("0","1").replace("1","2").replace("2","0")
        for i in n:
            s += i
            s += i
    R = int(s,3)
    if R > 120:
        print(N)
        break