from itertools import *
alf = "ABCt"
k = 0
for x in product(alf, alf,alf,alf,alf,alf):
    if x.count("t") == 2:
        k+=1
print(k)