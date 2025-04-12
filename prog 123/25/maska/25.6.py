from fnmatch import *
k = 0
m = []
for i in range(4899999972,0,-42):
    if fnmatch(str(i), "48*15*0"):
        k +=1
        m.append(i)
        if k == 5:
            break

m.sort(reverse=1)
for i in m:
    print(i)
print()
for i in m:
    print(i//42)