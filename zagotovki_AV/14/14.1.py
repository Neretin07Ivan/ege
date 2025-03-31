#x231y 12 +78x98y 14 .
for x in range(1,12):
    for y in range(12):
        s = int( (str(x) + "231" + str(y)),12) + int( ("78"+ str(x) + "98" + str(y)),14)
        if s % 99 == 0:
            print(s/99)
            break