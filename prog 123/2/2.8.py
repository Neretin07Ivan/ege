def f8(x):
    s = ""
    while x > 0:
        s = str(x%8) + s
        x = x//8
    return s
rmin = 10**10
for N in range(483,10**5):
    n= f8(N)
    s = sum([int(i) for i in n])
    if s % 2 == 0:
        n += f8(s)
    else:
        n = f8(s) + n
    R = int(n,8)
    if R < rmin:
        rmin = R
print(rmin)