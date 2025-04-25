from sys import *
from functools import lru_cache
setrecursionlimit(10**9)
@lru_cache(maxsize=10**9, typed=False)
def f(n,x):
    if n == x:
        return 1
    if n < x:
        return 0
    if n % 3 != 0:
        return f(n - 5, x) + f(n//3*3,x)
    else:
        return f(n - 5, x) + f(n//3,x)
print(f(103,73) * f(73,24))
