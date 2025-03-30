s = open(r"/Users/user/Public/demo_2025_17.txt").readlines()
s = [int(i) for i in s]
ms = min(s)
k = 0
mp = []
for i in range(len(s)-1):
    if s[i] % 16 == ms or s[i + 1] % 16 == ms:
        k+=1
        mp.append(s[i]+s[i+1])
print(k,max(mp))