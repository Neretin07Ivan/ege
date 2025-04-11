B = range(101,144)
C = range(144,200)
m = []
for an in [101,143,144, 199]:
    for ac in [101,143, 144, 199]:
        A = range(an,ac+1)
        k = 0
        for x in range(-10000,10000):
            if ((x in A) <= ((x in B) or (x in C))):
                k += 1
        if k == 20000:
            print(an,ac)
            m.append(ac - an)
print(max(m))