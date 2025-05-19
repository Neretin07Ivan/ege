f = open(r"files/dz24.4.txt").readline().replace("D", "E").split("E")
print(max([len(i) for i in f]))


