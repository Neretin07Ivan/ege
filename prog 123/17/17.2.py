import math
f = open(r"files/17.txt")
m = []
for line in f:
    m.append(int(line))
k = 0
maxs = 0
max3 = 0
for i in m:
    if len(str(abs(i))) == 3:
        max3 = max(max3, i)
max3 = max3 **3
for i in range(len(m)-1):
    x1 = int(m[i])
    x2 = int(m[i+1])
    s1 = 0
    s2 = 0
    for i in str(abs(x1)):
        s1 += int(i)
    for i in str(abs(x2)):
        s2 += int(i)
    if (s1 % 5 == 0 and s2 % 5 != 0) or (s1 % 5 != 0 and s2 % 5 == 0):
        if abs(x1**2 - x2**2) >= max3:
            k +=1
            maxs = max(maxs, x1 + x2)
print(k, maxs)