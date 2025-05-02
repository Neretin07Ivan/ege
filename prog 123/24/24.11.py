
# f = open(r"files/24.11.txt").readline()
# f = f.replace("EB","x").replace("EC","x").replace("ED","x").replace("EF","x")
# f = f.replace("AB","x").replace("AC","x").replace("AD","x").replace("AF","x")
# kmax = 0
# for i in range(1, len(f)):
#     if f[i-1] == "x":
#         nach = i
#         k = 0
#         kx = 0
#         while nach < len(f):
#             if f[nach] == "x":
#                 kx += 1
#                 k += 1
#             if kx == 131:
#                 break
#             k += 1
#             nach += 1
#         kmax = max(kmax, k)
#         print(kmax)
# print(kmax)
def max_subsequence_with_pairs(filename):
    vowels = {'A', 'E'}
    consonants = {'B', 'C', 'D', 'F'}

    with open(filename, 'r') as file:
        s = file.read().strip()

    max_len = 0
    left = 0
    pair_count = 0

    for right in range(1, len(s)):
        prev_char = s[right - 1]
        current_char = s[right]
        if prev_char in vowels and current_char in consonants:
            pair_count += 1

        # Если количество пар превышает 130, двигаем левую границу
        while pair_count > 130:
            # Проверяем пару, которая выходит за границу окна
            if left < right and s[left] in vowels and s[left + 1] in consonants:
                pair_count -= 1
            left += 1

        # Обновляем максимальную длину
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len

    return max_len


filename = r"files/24.11.txt"  # Укажите путь к файлу
print(max_subsequence_with_pairs(filename))