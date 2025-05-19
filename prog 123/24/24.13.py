f = open(r"files/24var06.txt").readline()
f = f.split("A")
smax = 0
for i in range(len(f)-2):
    s = len(f[i])+len(f[i+1])+len(f[i+2])+2
    smax = max(smax, s)
print(smax)