s = "АВЕНС"
k = 0
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    m = x1 + x2 + x3 + x4 + x5
                    if m.count("Н") == 2 and len(set(list(m))) == 4:
                        k += 1
print(k)