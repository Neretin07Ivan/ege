def dell(x):
    dd = []
    for d in range(2,int(x**0.5)+1):
        if x % d == 0:
            dd.append(d)
            dd.append(x//d)
    dd = list(set(dd))
    return dd

def nat(x):
    for d in range(2,int(x**0.5)+1):
        if x % d == 0:
            return False
    else: return True

def f(x):
    m = dell(x)
    R = 0
    for i in m:
        if nat(i):
            R += i
    return R


k=0
for i in range(500_000, 10**10):
    R = f(i)
    if R > 2000 and R %10 == 7:
        k = k+1
        print(i)
    if k == 5:
        break
print()
k = 0
for i in range(500_000, 10**10):
    R = f(i)
    if R > 2000 and R %10 == 7:
        k = k+1
        print(R)
    if k == 5:
        break
