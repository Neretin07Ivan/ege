from fnmatch import *


def dell(n):
    d = []
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            d.append(i)
            d.append(n//i)
    d = list(set(d))
    res = []
    for i in d:
        if i%2 != 0:
            res.append(i)
    return res


def delln(n):
    if len(dell(n)) == 3:
        return True
    else:
        return False

k = 0
for i in range(100000,10**10):
    if fnmatch(str(i),'1*1?2'):
        if delln(i):
            print(i, sum(dell(i)))
            k+=1
            if k == 5:
                break