from fnmatch import *
for i in range(0,10**8,1991):
    if fnmatch(str(i),'2*1?71'):
        print(i)