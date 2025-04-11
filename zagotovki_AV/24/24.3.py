f = open(r"files/24.txt").readline().replace("3","e").replace("4","a").replace("yandex", "*")
maxa = 0
k = 0
for i in range(len(f)):
    if f[i] == "*":
        k += 6
    else:
        if k != 0:
            if f[i] == "y":
                k+=1
                if f[i + 1] == "a":
                    k += 1
                    if f[i + 2] == "n":
                        k += 1
                        if f[i + 3] == "d":
                            k += 1
                            if f[i + 4] == "e":
                                k += 1
                                if f[i + 5] == "x":
                                    k += 1
        maxa = max(maxa, k)
        k = 0
print(maxa)