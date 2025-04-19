# (x→y)∧(w∨(¬w))
print("x y w")
for x in range(2):
    for y in range(2):
        for w in range(2):
            if not (x <= y) and (w or (not w)):
                print(x,y,w)
print(len(bin(10**13)))