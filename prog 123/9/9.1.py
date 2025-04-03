m = [[int(x) for x in line.split()] for line in open(r"files/9.1.txt").readlines()]
k = 0
for line in m:
    print(*line)
    a = sorted(line)
    if (min(a)+max(a))**2 > (a[1]**2 + a[2]**2 + a[3]**2):
        k += 1
print(k)