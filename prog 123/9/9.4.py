m = [[int(x) for x in line.split()] for line in open(r"files\9.2.txt")]
k = 0

for i in m:
    a = sorted(i)
    k += 1
    if max(i) < (sum(i) - max(i)):
        if a[0] + a[3] != a[1] + a[2]:
            print(k)