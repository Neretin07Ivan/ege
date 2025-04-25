s = open(r"files/24.2.txt").readline()
max_len = 0
for i in range(len(s) - 1):
    if s[i] == '7' and s[i + 1] == '8':
        left = i
        right = i + 2
        current_num = 78
        temp_num = 78
        temp_left = left
        while temp_left >= 1:
            prev_num = temp_num - 1
            prev_str = str(prev_num)
            prev_len = len(prev_str)
            if temp_left - prev_len >= 0 and s[temp_left - prev_len:temp_left] == prev_str:
                temp_left -= prev_len
                temp_num = prev_num
            else:
                break


        temp_num = 78

        temp_right = right
        while temp_right <= len(s) - 1:
            next_num = temp_num + 1
            next_str = str(next_num)
            next_len = len(next_str)
            if temp_right + next_len <= n and s[temp_right:temp_right + next_len] == next_str:
                temp_right += next_len
                temp_num = next_num
            else:
                break

        current_len = temp_right - temp_left
        if current_len > max_len:
            max_len = current_len

print(max_len)