for N in range(0,10**8):
    n = bin(N)[2:]
    if str(n).count("1")%2 == 0:
        n = str(n) + "0" * str(n).count("0")
    else:
        n = str(n) + "1" * str(n).count("1")
    R = int(n,2)
    if R >2000:
        print(N)
        break