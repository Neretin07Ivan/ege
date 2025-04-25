s1 = []
for i in range(16):
    n = str(bin(i)[2:])
    n = (4 - len(n)) * "0" + n
    s = "1" * 28 + n
    s1.append(s)
s2 = []
for i in range(2**6):
    n = str(bin(i)[2:])
    n = (6 - len(n)) * "0" + n
    s = "1" * 26 + n
    s2.append(s)
k = 0
for i in s1:
    if i not in s2:
        k += 1
for i in s2:
    if i not in s1:
        k += 1
print(k)

print(2**32)
print(1024**3 *4)