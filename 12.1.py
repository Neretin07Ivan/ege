max1 = 0
for i in range(201,10000):
    s = "1" * i
    while "1111" in s:
        s = s.replace("1111", "22",1)
        s = s.replace("222","1",1)
    if max1 < s.count("1"):
        max1 = s.count("1")
        maxi = i
        print(max1, maxi)

