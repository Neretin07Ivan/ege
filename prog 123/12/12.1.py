s = "=" + "1" * 11 + 12 * "2" + 13 * "3"
while "=1" in s or "=2" in s or "=3" in s:
    if "=1" in s:
        s = s.replace("=1","22=")
    if "=2" in s:
        s = s.replace("=2","2=")
    if "=3" in s:
        s = s.replace("=3","1=")
print(s.count("1")+ s.count("2") * 2+ s.count("3") * 3)