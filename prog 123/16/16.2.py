import sys
from functools import lru_cache
sys.setrecursionlimit(10**9)
@lru_cache(maxsize=10**9, typed=False)
def f(n):

    if n == 1:
        return 2
    if n > 1 and f(n-1) < 7555444:
        return f(n-1) + 6
    return f(n-1) - 7555444

m = []
for i in range(10000, 7555444):
    s = f(i)
    if s == 7555442:
        print(i)
        break
