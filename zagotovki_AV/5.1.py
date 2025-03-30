for s in range(99,1000000):
    n = s
    s = bin(s)[2:]
    for i in range(3):
        if s.count("0") > s.count("1"):
            s += "1"
        elif s.count("0") < s.count("1"):
            s += "0"
        else:
            s += str(int(s)%10)
    s = int(s,2)
    if s % 4 == 0:
        print(n)
        break

