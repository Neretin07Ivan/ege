from fnmatch import *
k = 0
m = []
for i in range(1800000000, 0,-1):
    if sum(map(int, list(str(i)))) % 11 == 0:
        if fnmatch(str(i), "17*023?9"):
            k += 1
            m.append(i)
    if k == 5:
        break
for i in sorted(m):
    print(i)
print()
for i in sorted(m):
    print(sum(map(int, list(str(i))))//11)
