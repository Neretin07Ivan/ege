m = [[int(x) for x in line.split()] for line in open(r"files\9.3.txt")]
k = 0
for i in m:
    a = sorted(i)
    k += 1
    povt = [a.count(x) for x in a]
    if povt.count(2) == 4 and povt.count(1) == 3:
        if a.count(max(a)) == 1:
            print(sum(a),end="")
            break