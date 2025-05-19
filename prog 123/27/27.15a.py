f = open(r"files/27_15_А.txt").readlines()
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
for i in f:
    if i[1] < 2 - i[0] ** 2:
        if i[1] >= i[0]:
            if i[0] > 0 and i[1] > 0:
                c1.append(i)
            elif i[0] < 0 and i[1] < 0:
                c2.append(i)
k1 = cent(c1)
k2 = cent(c2)
print((abs((float(k1[0]) + float(k2[0])))*10000//2))
print(abs((float(k1[1]) + float(k2[1])))*10000//2)