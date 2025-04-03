m = [[int(x) for x in line.split()] for line in open(r"files\9.4.txt")]
k = 0
for i in m:
    a = sorted(i)
    if [a.count(x) for x in a].count(1) < 6:
        if a.count(min(a)) == 1:
            if max(a) / ((sum(a) - max(a)) / 5) > 3:
                k += 1
print(k)