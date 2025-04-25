f = "ABCDUUABCDADADADUBADC"
f = f.replace("C","B").replace("D","B").replace("U","A")
print(f)
while "BB" in f or "AA" in f:
    f = f.replace("BB"," B")
    f = f.replace("AA","A ")
print(f)
f = f.split()
print(len(max(f,key = len))//2)
