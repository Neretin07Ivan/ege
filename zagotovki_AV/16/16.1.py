from sys import setrecursionlimit
setrecursionlimit(10000)
def F(n):
    if n == 1:
        return 3
    else:
        return F(n-1) *(n-1)
print(F(6))