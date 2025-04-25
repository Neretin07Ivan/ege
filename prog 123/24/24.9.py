f = open(r"files/24_23osn.txt").readline()
s = f.replace("A","1").replace("B","2").replace("C","3").replace("D","4").replace("E","5").replace("F","6")
k = 0
kmax = 0
for i in range(len(s)):
    if s[i].isdigit():
        k += 1
        kmax = max(kmax, k)
    else:
        k = 0
print(kmax)