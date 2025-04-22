f = open(r'files/26-112.txt')
n = list(map(int,f.readline().split()))[0]
f = sorted([list(map(int,i.rstrip("\n").split())) for i in f.readlines()], key=lambda x: x[0])
bank = [-1] * n
res1 = 0
res2 = 0
maxt = 0
kolch = [0] * n
posled = 0
for i in f:
    nach, fin = i
    kolch[bank.index(min(bank))] += 1
    if min(bank) <= nach:
        bank[bank.index(min(bank))] = nach + fin
    else:
        if bank.index(min(bank)) == 2:
            posled = fin
        bank[bank.index(min(bank))] = min(bank) + fin
        maxt = max(maxt, min(bank) - nach)
print(maxt, bank[kolch.index(max(kolch))] - posled)


