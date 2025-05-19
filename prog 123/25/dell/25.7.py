def pr(x):
    for i in range(2,int(x**0.5)+1):
        if int(x) % int(i) == 0:
            return False
    return True

def dell(x):
    d = []
    for i in range(2,int(x**0.5)+1):
        if int(x) % i == 0:
            d.append(i)
            d.append(x//i)
    d = list(set(d))
    return sum(d)

k = 0
for i in range(1_500_000,10**10):
    if pr(dell(i)):
        if dell(i) != 0:
            print(i)
            k = k+1
    if k == 5:
        break
print()
k = 0
for i in range(1_500_000,10**10):
    if pr(dell(i)):
        if dell(i) != 0:
            print(dell(i))
            k = k+1
    if k == 5:
        break
