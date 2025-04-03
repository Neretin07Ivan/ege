for i in range(1,1000):
    N = bin(i)[2:]
    if N.count('1') % 2 == 0:
        N += "0"
        N = "10" + N[2:]
    else:
        N += "1"
        N = "11" + N[2:]
    r = int(N,2)
    if r >= 24:
        print(i)
        break