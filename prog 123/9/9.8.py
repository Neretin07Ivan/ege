m = [[int(x) for x in line.split()] for line in open(r"files\9.8.txt")]
k = 0
for i in m:
    a = sorted(i)
    k += 1
    povt = [a.count(x) for x in a]
    if povt.count(2) == 2 and povt.count(1) == 4:
        for i in range(len(povt)):
            if povt[i] == 2:
                s = a[i]
                break
        if s > (sum(a) - s*2)/4:
            print(k)