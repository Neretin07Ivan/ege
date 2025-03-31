s = open(r"/Users/user/мое/17.txt").readlines()
m = 0
n = 0
k = 0
maxs = 0
res = 0
maxss = 0
for i in s:
    i = int(i)
    if i % 10 == 3:
        if (i**2) > maxs:
            maxs = i**2
for i in range(len(s)-1):
    m = int(s[i])
    n = int(s[i+1])
    if k != 0:
       if ((abs(m) % 10 == 0 and abs(n) % 10 != 3) or (abs(m) % 10 != 0 and abs(n) % 10 == 3)) and (m**2 + n**2) >= maxs:
           if (m**2 + n**2) > maxss:
               maxss = (abs(m)**2 + abs(i)**2)
           res +=1
    k += 1
print(res,maxss)

f = [abs(int(i)) for i in open("17.txt")]
max_element = max(f, key=lambda x: x if x % 10 == 3 else -10_000) ** 2
result = []
for i in range(len(f) - 1):
    c = 0
    if f[i] % 10 == 3:
        c += 1
    if f[i + 1] % 10 == 3:
        c += 1
    if c == 1 and f[i]**2 + f[i + 1]**2 >= max_element:
        result.append(f[i]**2 + f[i + 1]**2)
print(len(result), max(result))