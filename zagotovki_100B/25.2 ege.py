def dell(n):
    d = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if i != n//i:
                d.append(i)
                d.append(n//i)
            else:
                d.append(i)
    return len(sorted(d))

maxs = [0,0]
for i in range(124052, 124131):
    if dell(i) > maxs[0]:
        maxs[0] = dell(i)
        maxs[1] = i
print(maxs)