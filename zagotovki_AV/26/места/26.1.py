f = open(r"26-2.txt")
n = int(f.readline())
a = []
for i in range(n):
    x, y = [int(_) for _ in f.readline().split()]
    a.append([x, y])
a.sort()
ans = [0, 0]
for i in range(n - 1):
    if a[i][0] == a[i + 1][0] and a[i][1] == a[i + 1][1] - 3:
        row = a[i][0]
        seat = a[i][1] + 1
        if row > ans[0]:
            ans[0] = row
            ans[1] = seat

print(*ans)