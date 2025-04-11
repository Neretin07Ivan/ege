for i in range(3,10_001):
    s = "6" + i * "9"
    while "69" in s or "399" in s or "9999" in s:
        if "69" in s:
            s.replace("69", "9",1)
        if "399" in s:
            s.replace("399", "96",1)
        if "9999" in s:
            s.replace("9999", "3",1)
    print(s)
    print(map(int, list(s)))
    if sum(map(int, list(s))) == 54:
        print(i)