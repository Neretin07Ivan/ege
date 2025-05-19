f = open(r"files/24prob25.txt").readline()
s = f.split('A')
K = 100
su = K
for i in range(0, K+1):
    su += len(s[i])
maxt = su
for i in range(K + 1, len(s)):
    su = su - len(s[i - (K+1)]) + len(s[i])
    maxt = min(maxt, su)
print(maxt)