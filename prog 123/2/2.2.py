print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not((not x or not z)<= (x == y)):
                print(x,y,z)
                # zxy