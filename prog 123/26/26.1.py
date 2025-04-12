f = [i.rstrip("\n").split() for i in open("files/26-3.txt","r")]
m = {}
for i in f:
    if i[0] in m:
        m[i[0]].append(i[2])
    else:
        m[i[0]] = [i[2]]
k = 0
s = 0
for key in m:
    if len(m[key]) > 1:
        k+=1
        stav = []
        for i in m[key]:
            stav.append(int(i))
        stav = sorted(stav)[-2]
        s += int(stav)
print(k,s)