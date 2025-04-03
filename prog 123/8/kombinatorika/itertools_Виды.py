from itertools import *
alf = "ABC"
k = 0
for x in product(alf, repeat = 2):
    x = "".join(x)
    print(x)
    k+=1
print(k)

print()
k = 0
for x in permutations(alf, r = 2):
    x = "".join(x)
    print(x)
    k+=1
print(k)

print()
k = 0
for x in combinations(alf, r = 2):
    x = "".join(x)
    print(x)
    k+=1
print(k)