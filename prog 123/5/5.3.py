def F(n):
    string = ''
    while n > 0:
        string+=str(n%3)
        n//= 3
    return int(string[::-1])

for N in range(100000,0,-1):
    n = F(N)
    if str(n).count('2') > 0:
        n = str(n) + str(F(str(n).count('2')))
    else:
        n = str(n) + "0"
    if str(n).count('1') > 0:
        n = str(n) + str(F(str(n).count('1')))
    else:
        n = str(n) + "0"
    if str(n).count('0') > 0:
        n = str(n) + str(F(str(n).count('0')))
    else:
        n = str(n) + "0"
    R = int(n,3)
    if R < 1000:
        print(N)
        break
