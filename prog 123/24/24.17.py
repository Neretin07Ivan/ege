f = open(r"files/dz24.1.txt").readline()
k = 0
kmax = 0
for i in f:
    if i == "C":
        k += 1
    else:
        kmax = max(kmax, k)
        k = 0
print(kmax)