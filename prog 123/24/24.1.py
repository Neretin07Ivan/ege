f = open(r"files/24.1.txt").readline()

s = ""
smax = 0
for i in range(len(f)):
    if str(f[i]).isdigit():
        s += f[i]
    else:
        if s != "" and int(s) % 2 == 0:
            smax = max(smax, int(s))
        s = ""
print(smax)
