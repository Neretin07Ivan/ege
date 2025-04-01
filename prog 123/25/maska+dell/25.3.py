def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def dell(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if i != n//i:
                if prime(i):
                    if prime(n//i):
                        return True
    return False


k = 0
m = 10**10
for i in range(268312, 336492+1):
    if dell(i):
        k += 1
        m = min(m,i)
print(k,m)