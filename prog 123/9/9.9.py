f = open(r"files/9.9.txt").readlines()
f = [i.rstrip("\n").split("\t") for i in f]
k = 0
for x in range(len(f)):
    for y in range(len(f[x])):
        s = []
        if y < 9:
            s.append(f[x][y + 1])
        if y > 0:
            s.append(f[x][y - 1])
        if x + 1 < len(f):
            s.append(f[x + 1][y])
            if y  < 9:
                s.append(f[x + 1][y + 1])
            if y > 0:
                s.append(f[x + 1][y - 1])
        if x > 0:
            s.append(f[x - 1][y])
            if y < 9:
                s.append(f[x - 1][y + 1])
            if y >0:
                s.append(f[x - 1][y - 1])
        current = int(f[x][y])
        condition1 = all(current >= int(n) for n in s)
        condition2 = any(current == int(n) for n in s)
        if condition1 and condition2:
            k += current
print(k)