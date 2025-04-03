alf = "деилнфь"
# ф = 5 ь = 6
res = 0
k = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        s = str(x1) + str(x2) + str(x3) + str(x4) + str(x5) + str(x6)
                        k+=1
                        if s[0] != "ь" and s.count("ф") == 2 and k %2 == 0:
                            res += 1
print(res)

