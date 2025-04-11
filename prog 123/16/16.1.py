import sys
from functools import lru_cache

sys.setrecursionlimit(10**9)
@lru_cache(maxsize=10000, typed=False)
def f(n):
    if n>=2024:
        return 1
    return f(n+2) + f(n+4)


m = set()
for i in range(1,10**4):
    m.add(f(i))
print(len(m))
