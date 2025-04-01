def prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def dell2(n, n1):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if i != n//i:
                if i != n1:
                    if n//i != n1:
                        if prime(i):
                            if prime(n//i):
                                return True
    return False



def dell(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and prime(i):
            if dell2(n // i, i):
                return True
    return False

k = 0
m = 0
for i in range(105673, 220785):
    if dell(i):
        k += 1
        m = max(m, i)
print(k,m)
