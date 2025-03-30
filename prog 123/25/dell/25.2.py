def dell(n):
    d = []
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            d.append(i)
            d.append(n//i)
    d = list(set(d))
    if len(d)>1:
        return max(d)-min(d)
    else:
        return 0


k = 0
for i in range(850_000, 10**10):
    if dell(i) != 0 and dell(i) % 5 == 0:
        k += 1
        print(i, dell(i))
        if k == 6:
            break