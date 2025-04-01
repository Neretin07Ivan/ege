from fnmatch import *

def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True



for i in range(0,10**9,1234):
    if fnmatch(str(i),'24?127*0'):
        pi = 0
        for j in str(i):
            pi *= int(j)
        if pi > 1:
            if prime(pi):
                print(i, i //1234 )


