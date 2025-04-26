for x in range(15):
    s1 = int("12305",15) + x * 15
    s2 = int("10233",15) + x * 15**3
    s = s1 + s2
    if s%14 == 0:
        break
s1 = int("12305",15) + x * 15
s2 = int("10233",15) + x * 15**3
s = s1 + s2
print(s // 14)