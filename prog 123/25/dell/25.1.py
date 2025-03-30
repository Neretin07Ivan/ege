def dell(n):
    d = []
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            d.append(i)
            d.append(n//i)
    return sorted(list(set(d)))

for i in range(258274, 258297):
    if len(dell(i)) == 2:
        print(dell(i))