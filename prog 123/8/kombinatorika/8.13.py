s = "В, Е, Н, О, С, Т, Ч, Ь"
s = s.split(", ")
k = 0
kk = []
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    for x6 in s:
                        sl = x1 + x2 + x3 + x4 + x5 + x6
                        k += 1
                        if k % 2 == 0 and sl[0] in ["Е", "О", "Ь"] and sl.count("О") >= 2:
                            kk.append(sl)
print(len(kk))