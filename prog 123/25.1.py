from fnmatch import * #подключаем библиотеку fnmatch
for x in range(0, 10**10, 2024):
    if fnmatch(str(x), '3?2758*4'): #проверяем строчное число на нашу маску
        print(x)