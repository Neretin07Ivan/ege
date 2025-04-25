for a in range(1, 10000):
    A = []
    for x in range(10000):
        if x % a == 0:
            A.append(x)
    if all(((x % 3 == 0) <= ((x % 5 == 0) <= ((x % 3 == 0) and (x in A)))) for x in range(10000)):
        print(a)