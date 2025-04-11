
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


f = [i.rstrip("\n").replace(",",".").split(" ") for i in open(r"files/27_3_B.txt").readlines()]
k1 = []
k2 = []
k3 = []
k4 = []
for i in f:
    if float(i[0]) < 0 and float(i[1]) > 4:
        k1.append(i)
    elif float(i[0]) < 0 :
        k2.append(i)
    elif float(i[1]) < 1.1 :
        k3.append(i)
    else:
        k4.append(i)

c1 = cent(k1)
c2 = cent(k2)
c3 = cent(k3)
c4 = cent(k4)

Sx = float(c1[0]) + float(c2[0]) + float(c3[0]) + float(c4[0])
Sy = float(c1[1]) + float(c2[1]) + float(c3[1])+ float(c4[1])
print(Sx * Sx * 10000)
print(Sy * Sy * 10000)