
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
def mr(k,t):
    xmax = 0
    ymax = 0
    for j in range(len(k)):
        x1 = float(k[j][0])
        y1 = float(k[j][1])
        x2 = float(t[0])
        y2 = float(t[1])
        xmax = max(abs(x1 - x2), xmax)
        ymax = max(abs(y1 - y2), ymax)
    return (xmax, ymax)


f = [i.rstrip("\n").replace(",",".").split("\t") for i in open(r"files/27_6_B.txt").readlines()]
k1 = []
k2 = []
k3 = []
for i in f:
    if float(i[0]) > 5:
        k1.append(i)
    elif float(i[1]) > 6:
        k2.append(i)
    else:
        k3.append(i)
c1 = cent(k1)
print(c1)
c2 = cent(k2)
print(c2)
c3 = cent(k3)
print(c3)
m1 = mr(k1,c1)
m2 = mr(k2,c2)
m3 = mr(k3,c3)
x = max(m1[0],m2[0],m3[0])
y = max(m1[1],m2[1],m3[1])
print(int(x*10000), int(y*10000))


