f =  [list(map(int, i.split("\t"))) for i in open(r"files/9.10.txt").readlines()]
k = 0
for i in f:
    if len(set(i)) == 4:
        ss = [x ** 2 for x in i]
        if (max(i) + min(i))**2 < sum(ss) - max(ss) - min(ss):
            k += 1
print(k)
