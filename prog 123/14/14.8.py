def f5(n):
    s = ""
    while n > 0:
        s = str(n % 5) + s
        n = n//5
    return s

sx = 0
maxx = 0
for x in range(1,2031):
    s = f5(5 ** 100 - x)
    if s.count("0") > sx:
        sx = s.count("0")
        maxx = x
print(maxx,sx)