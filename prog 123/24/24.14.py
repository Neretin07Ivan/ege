f = open(r"files/24var06.txt").readline()
s = f.split('A')
K = 140
su = K
for i in range(1, K):
    su += len(s[i])
maxt = su
for i in range(K + 1, len(s)):
    su = su - len(s[i - (K)]) + len(s[i-1])
    maxt = min(maxt, su)
print(maxt)