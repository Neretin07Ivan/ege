gl = "уа"
sogl = "мк"
alf = gl + sogl
k = 0
for x1 in sogl:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in gl:
                    s = x1+x2+x3+x4+x5
                    k += 1

print(k)
