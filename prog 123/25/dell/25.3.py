def dell(n):
    d = []
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            d.append(i)
            d.append(n//i)
    d = list(set(d))
    if len(d) > 2:
        return max(d) + min(d)
    else:
        return 0

k = 0
for i in range(800_000 + 1, 10**10):
    if dell(i) % 10 == 8:
        k += 1
        print(i, dell(i))
        if k == 5:
            break