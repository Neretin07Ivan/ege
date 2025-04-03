from itertools import *
k = 0
for i in permutations("01234567", r=5):
    if i[0] != "0":
        s = "".join(i)
        for j in s:
            if int(j)%2 == 0:
                s = s.replace(j,"2")

            else:
                s = s.replace(j,"1")
        if "22" not in s and "11" not in s:
            k += 1
print(k)
