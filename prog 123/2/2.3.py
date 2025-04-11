print(4*2**0.5)

for N in range(1000,10000):
    if len(set(str(N))) == 4:
        n = sorted(list(str(N)))
        x1 = int(n[0]) + int(n[3])
        x2 = int(n[1]) * int(n[2])
        R = []
        R.append(str(x1))
        R.append(str(x2))
        R = "".join(sorted(R))
        if int(R) > 85:
            print(N)
            exit(0)
