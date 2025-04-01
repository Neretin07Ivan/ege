for i in range(10):
    for j in range(100):
        for z in range(10):
            s = '1' + str(i) + '2' + str(j).zfill(2) + '3' + str(z) + '0'
            if int(s) <= 10**8 and int(s) % 2022 == 0:
                print(s, int(s) // 2022)

print("***")
from fnmatch import *
for i in range(0,10**8,2022):
    if fnmatch(str(i), "1?2??3*0"):
        print(i, int(i) // 2022)
