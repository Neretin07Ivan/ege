def dell(n):
    d = []
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            d.append(i)
            d.append(n//i)
    return sorted(list(set(d)))

k = 0
for i in range(800_000, 10**10):
    s = dell(i)
    for d in s:
        if d % 100 == 14 and d != 14:
            k += 1
            print(i)
            break
    if k == 5:
        break
k = 0
print()
for i in range(800_000, 10**10):
    s = dell(i)
    for d in s:
        if d % 100 == 14 and d != 14:
            k += 1
            print(d)
            break
    if k == 5:
        break