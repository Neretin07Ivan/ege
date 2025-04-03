m = [[int(x) for x in line.split()] for line in open(r"files\9.5.txt")]
k = 0
for i in m:
    a = sorted(i)
    povt = [a.count(x) for x in a]
    if povt.count(2) == 4 and povt.count(1) == 3 and sum([a[i] for i in range(len(povt)) if povt[i] == 2])/4 > sum(a)/7:
        k += 1
print(k)
