alf = "пирог"
k = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                s = x1+x2+x3+x4
                if s.count("о") <= 2:
                    if "о" in s:
                        if s[0] != "о" and "ио" not in s and "оо" not in s:
                            print(s)
                            k += 1
                    else:
                        k += 1
print(k)