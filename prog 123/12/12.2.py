s = "0" * 45 +"2" * 45 + 45 * "3"
while "02" in s or "32" in s or "30" in s:
    if "02" in s:
        s = s.replace("02","20")
    if "32" in s:
        s = s.replace("32","23")
    if "30" in s:
        s = s.replace("30","03")
print(s[14]+s[74]+s[114])
