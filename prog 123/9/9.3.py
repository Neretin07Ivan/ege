m = [[int(x) for x in line.split()] for line in open(r"files\9.2.txt")]
k = 0
for i in m:
    if max(i) < (sum(i) - max(i)):
        if len(set(i)) == 3:
            k += 1
print(k)