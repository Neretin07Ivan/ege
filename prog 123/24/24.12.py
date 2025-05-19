f = open(r"files/24var06.txt").readline()
f = f.split("A")
smax = 0
for i in range(len(f)-1):
    s1 = len(f[i])
    s2 = len(f[i+1])
    smax = max(smax, s1+s2+1)
print(smax)