# Маша составляет слова из шести букв, в которых есть только буквы из слова ГИПЕРБОЛА,
# причём на первом и последнем месте не может быть гласной вообще, а на любой другой позиции
# она не может быть с двух сторон окружена согласными. То есть сочетание БОЛ не может встречаться в слове,
# а словосочетания АОЛ или БОИ может. Каждая из других допустимых букв может встречаться в слове любое количество
# раз или не встречаться совсем.
# Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
alf = "гипербола"
sogl = "гпрбл"
gl = "иеоа"
k = 0
for x1 in sogl:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in sogl:
                        m = []
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        for i in range(len(s)):
                            if s[i] in gl:
                                m.append("2")
                            else:
                                m.append("1")
                        m = "".join(m)
                        if "121" not in m:

                            k += 1

print(k)


