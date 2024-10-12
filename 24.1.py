s = open(r'/Users/user/Downloads/24.txt').readlines()
min = s[0]
k=0
for line in s:
    line.count("G")
    if line.count("G")< min.count("G"):
        min = line
alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
max=0
for i in alf:
    if min.count(i)>=max:
        A=i
        print()
        max=min.count(i)
print(A)