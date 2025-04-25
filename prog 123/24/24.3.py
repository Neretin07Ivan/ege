f = open(r"files/24_23dosr.txt").readline()
f = f.replace("D","B").replace("C","B").replace("BB","B B")
while "BB" in f:
    f = f.replace("BB","B B")
f = f.split()
maxl = 0
for i in f:
    maxl = max(maxl, len(i))
print(maxl)