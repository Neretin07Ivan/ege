#((x∣42>64)∧(x∣34≤102))→¬(x∣А<70)
for A in range(1000):
    k = 0
    for x in range(1,1001):
        if ((x|42>64)and(x|34<=102)) <= (not( x|A <70)):
            k += 1
    if k == 1000:
        print(A)
        break

