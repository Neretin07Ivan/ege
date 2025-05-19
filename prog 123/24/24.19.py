# Доступен файл для чтения: 24.txt
f = open("24.txt").readline()

f = f.replace("G"," ").replace("H"," ").replace("I"," ").replace("J"," ")
f = f.replace("K"," ").replace("L"," ").replace("M"," ").replace("N"," ")
f = f.replace("O"," ").replace("P"," ").replace("R"," ").replace("S"," ")
f = f.replace("Q"," ").replace("T"," ").replace("U"," ").replace("V"," ")
f = f.replace("W"," ").replace("X"," ").replace("Y"," ").replace("Z"," ")
f = f.split()

maxk = 0
for i in f:
    k = 0
    if len(i) >= 6:
        k = len(i)//6
    maxk = max(maxk,k)
print(maxk)