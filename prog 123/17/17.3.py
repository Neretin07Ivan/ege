f = [int(i.rstrip("\n")) for i in open(r"files/17.txt").readlines()]
maxf = 0
for i in f:
    if len(str(abs(i))) == 4:
        maxf = max(maxf, i)
k = 0
maxs = 0
for i in range(len(f)-2):
    x1 = f[i]
    x2 = f[i+1]
    x3 = f[i+2]
    l = 0
    if x1 % 10 == 3 or x1 % 10 == 5:
        l += 1
    if x2 % 10 == 3 or x2 % 10 == 5:
        l += 1
    if x3 % 10 == 3 or x3 % 10 == 5:
        l += 1
    if (l > 1) and ((x1 * x2 * x3) <= (maxf**3)):
        k += 1
        maxs = max(maxs, x1 + x2 + x3)
print(k, maxs)


f = [int(i) for i in open(r"files/17.txt").read().split()]
max4 = max(x for x in f if 1000 <= abs(x) <= 9999)
max_cubed = max4 ** 3
k = max_sum = 0

for i in range(len(f)-2):
    a, b, c = f[i], f[i+1], f[i+2]
    count = sum(1 for x in [a, b, c] if x % 10 in {3, 5})
    if count >= 2 and a * b * c <= max_cubed:
        k += 1
        current_sum = a + b + c
        if current_sum > max_sum:
            max_sum = current_sum
print(k, max_sum)
