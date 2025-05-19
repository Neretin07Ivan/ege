f = open(r"files/24var04.txt").readline()
maxt = 0
for s in f.split('E'):
    K = 500
    if s.count("A") < K:
        maxt = max(maxt, len(s))
    else:
        s = s.split('A')
        su = K
        for i in range(0, K + 1):
            su += len(s[i])
        maxt = max(maxt, su)
        for i in range(0, len(s) - (K + 1)):
            su = su - len(s[i]) + len(s[i + K + 1])
            maxt = max(maxt, su)
print(maxt)