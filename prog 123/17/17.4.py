f = [int(i.rstrip("\n")) for i in open(r"17.txt").readlines()]
maxx = 0
for i in f:
    if i % 36 == 0:
        maxx = max(maxx, i)
k = 0
min_sum = float('inf')
for i in range(len(f) - 2):
    x1, x2, x3 = f[i], f[i + 1], f[i + 2]
    c = 0
    if x1 > 0 or x1 % 100 == 36:
        c += 1
    if x2 > 0 or x2 % 100 == 36:
        c += 1
    if x3 > 0 or x3 % 100 == 36:
        c += 1

    if c >= 2:
        sums = x1 + x2 + x3
        if sums <= maxx:
            k += 1
            if sums < min_sum:
                min_sum = sums
print(k, min_sum)

print(1241561 % 100)
print(-1241561 % 100)