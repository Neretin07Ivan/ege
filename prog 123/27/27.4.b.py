
def dist(x1,x2,y1,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


def cent(KL):
    t = 0
    tmax = 0
    kmax = 0
    for i in range(len(KL)):
        t = KL[i]
        k = 0
        for j in range(len(KL)):
            x1 = float(KL[j][0])
            y1 = float(KL[j][1])
            x2 = float(t[0])
            y2 = float(t[1])
            if dist(x1,x2,y1,y2) < 2.1:
                k +=1
        if k >= kmax:
            if k != kmax:
                kmax = k
                tmax = t
            else:
                x1 = float(tmax[0])
                y1 = float(tmax[1])
                x2 = float(t[0])
                y2 = float(t[1])
                if dist(x1, 0, y1, 0) > dist(x2, 0, y2, 0):
                    tmax = t
    return tmax


f = [i.rstrip("\n").replace(",",".").split(" ") for i in open(r"files/27_4_Б.txt").readlines()]
k1 = []
k2 = []
k3 = []
for i in f:
    if float(i[0]) < -2 and float(i[1]) < 2.5:
        k1.append(i)
    elif float(i[1]) < 2 and float(i[0]) > 1:
        k2.append(i)
    elif float(i[0]) >3:
        k2.append(i)
    else:
        k3.append(i)
c1 = cent(k1)
c2 = cent(k2)
c3 = cent(k3)
print(c1,c2,c3)
Cx = abs(int((float(c1[0]) + float(c2[0]) + float(c3[0]))*10000//3))
Cy = abs(int((float(c1[1]) + float(c2[1]) + float(c3[1]))*10000//3))
print(Cx, Cy)