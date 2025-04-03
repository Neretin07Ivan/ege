from itertools import *
ch = "02468"
nch = "13579"
k = 0
for i in product("2468","13579","02468","13579"):
    k += 1
for i in product("13579","02468","13579","02468"):
    k += 1
print(k)