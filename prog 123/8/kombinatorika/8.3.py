from itertools import *
alf = "ABC"
k = 0
for x in product(alf, alf,alf,alf,"ABCX"):
    k+=1
print(k)