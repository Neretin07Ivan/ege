s = open(r'/Users/user/Public/24.txt').readline()
k = 0
mn = []

for i in range(len(s)-1):
    if s[i] == "A":
        if s[i+1] in "ABC":
            i+=1
            mn.append(k)
            k = 1
        else:
            k+=1
    elif s[i] == "B":
        if s[i+1] in "ABC":
            i+=1
            mn.append(k)
            k = 1
        else:
            k+=1
    elif s[i] == "C":
        if s[i+1] in "ABC":
            i+=1
            mn.append(k)
            k = 1
        else:
            k+=1
    else:
        k+=1
print(max(mn))

