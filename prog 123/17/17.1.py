f = [int(x) for x in open("files/17.txt","r")]
m = []
for line in f:
    if len(str(line)) == 3:
        m.append(line)
min3 = 132
maxs = 0
k = 0
for i in range(len(f)-1):
    x1 = f[i]
    x2 = f[i+1]
    if (x1 + x2) < min3**2:
        maxs = max(maxs, x1 + x2)
        k += 1
print(k, maxs)


