from sys import setrecursionlimit
setrecursionlimit(10000)
def F(n):
    if n == 1:
        return 1
    else:
        return n*F(n-1)
print(F(2023)/F(2020))