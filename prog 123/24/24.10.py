import string
f = open(r"files/24.10.txt").readline()
a = string.ascii_lowercase
for i in a:
    f = f.replace(i, " ")
print(a)
while "+ " in f or " +" in f or "++" in f:
    f = f.replace("++", " ").replace("+ ", " ").replace(" +", " ")
f = f.split()
print(f)
print(len(max(f, key=len)))