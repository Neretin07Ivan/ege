f = open(r"files/24_23dosr.txt").readline()
f = f.replace("M", "P").replace("N","P").replace("O","P")
while "PPP" in f:
    f = f.replace("PPP","PP PP")
f = f.split()
print(len(max(f,key=len)))
