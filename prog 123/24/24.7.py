f = open(r"files/24_1.txt").readline()
while "ABB" in f:
    f = f.replace("ABB","AB BB")
f = f.split()
print(len(max(f,key = len)))