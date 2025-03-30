for i in range(10):
    s = "1" + str(i) + "954" + "21"
    if int(s) % 3023==0:
        print(s)
    s = "1" + str(i) + "954" + "021"
    if int(s) % 3023 == 0:
        print(s)
    s = "1" + str(i) + "954" + "0021"
    if int(s) % 3023 == 0:
        print(s)
    for t in range(1000):
        s="1"+str(i)+"954"+str(t)+ "21"
        if int(s) % 3023==0:
            print(s)
