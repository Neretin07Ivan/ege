for A in range(10**10):
    k = 0
    y = 100000
    for x in range(y):
        if (x & 91 == 0) or ((x & 77 == 0) <= (x & A != 0)):
            k += 1
    if k == y:
        print(A)
        break