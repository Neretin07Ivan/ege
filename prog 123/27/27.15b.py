f = open(r"files/27_15_Б.txt").readlines()
for i in range(len(f)):
    f[i] = f[i].replace(",",".").replace("\n","").split("\t")
    f[i] = list(map(float,f[i]))


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

c1 = []
c2 = []
c3 = []
c4 = []
for i in f:
    x = i[0]
    y = i[1]
    if dist(0,x,0,y) > 1:
        if y < 1:
            if y > 0 and x > 0:
                if y > x - 1:
                    c1.append(i)
    if dist(0,x,0,y) > 1:
        if y < 1:
            if y < 0 and x < 0:
                if y > x - 1:
                    c2.append(i)
    if dist(0,x,0,y) < 1:
        if y < 1:
            if y < 0 and x > 0:
                if y < x - 1:
                    c3.append(i)
    if dist(0,x,0,y) < 1:
        if y < 1:
            if y > 0 and x < 0:
                if y > x - 1:
                    c4.append(i)
k1 = cent(c1)
print(k1)
k2 = cent(c2)
print(k2)
k3 = cent(c3)
print(k3)
k4 = cent(c4)
print(k4)
print(abs((float(k1[0]) + float(k2[0]) + float(k3[0]) + float(k4[0])))*10000//4)
print(abs((float(k1[1]) + float(k2[1]) + float(k3[1]) + float(k4[1])))*10000//4)