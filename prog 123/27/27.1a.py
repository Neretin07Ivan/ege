
def dist(x1,x2,y1,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5



def cent(k):
    smin = 10**10
    tmin = 0
    for i in range(len(k)):
        t = k[i]
        s = 0
        for j in range(len(k)):
            x1 = float(k[j][0])
            y1 = float(k[j][1])
            x2 = float(t[0])
            y2 = float(t[1])
            s += dist(x1,x2,y1,y2)
        if s < smin:
            smin = s
            tmin = t
    return tmin







f = [i.rstrip("\n").replace(",",".").split("\t") for i in open(r"files/27.1_a.txt").readlines()]
k1 = []
k2 = []
k3 = []
for i in f:
    if float(i[1]) > 15:
        k1.append(i)
    else:
        k2.append(i)
print(cent(k1))
print(cent(k2))
print((float(cent(k1)[0]) + float(cent(k2)[0]))/2*10000)
print((float(cent(k1)[1]) + float(cent(k2)[1]))/2*10000)