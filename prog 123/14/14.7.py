for x in range(21):
    for y in range(21):
        s1 = int("12009",21) + x * 21 + y *21**2
        s2 = int("36099",21) + y *21 **2
        s = s1 + s2
        if s % 18 != 0:
            break
    else:
        break

s1 = int("12009",21) + x * 21 + 5 *21**2
s2 = int("36099",21) + 5 *21 **2
s = s1 + s2
print(s // 18)
