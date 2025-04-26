n = 4 ** 2018 + 8 ** 305 - 2**130 - 120
n = f"{n:b}"
print(str(n).count("1"))