f = open(r"files/24.3.txt").readline()
k = 0
print(f)
k = 1
kmax = 1
for i in range(1, len(f)-1):
    if f[i+1] > f[i] or (f[i+1] == "a" and f[i] == "Z"):
        k += 1
        kmax = max(kmax,k)
    else:
        k = 1
print(kmax)


