alf = "комбайн"
k = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        for x7 in alf:
                            s = x1+x2+x3+x4+x5+x6+x7
                            if len(set(s)) == 7:
                                if s[0] != "й":
                                    if "ай" not in s:
                                        k += 1
print(k)