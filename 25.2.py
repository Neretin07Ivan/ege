mn = set()
for A in range(100):
    for x in range(30):
        for y in range(30):
            if not ((2*x + 3*y > 30) or (x + y <= A)):
                mn.add(str(A))

m = [int(i) for i in mn]
m = sorted(m)
print(m)


