f = open(r"files/24_22osn_PNO.txt").readline()
s = f[:]
s = s.replace("PNO","***").replace("NPO","***").replace("N","P").replace("O","P").split("P")
print(len(max(s,key=len)))