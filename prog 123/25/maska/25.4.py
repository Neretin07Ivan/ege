from fnmatch import *
for i in range(10**8,1300000000, 31):
    if fnmatch(str(i),'12345?7?8'):
        print(i)