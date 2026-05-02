def solution(s):
    answer = 0
    cnt = 0
    new_s = ""
    for i in range(1,len(s)//2+1):
        cur_char = s[::i]
        while cur_char in s:
            cnt += 1
            new_s += str(cnt) + cur_char
    return answer

print(solution('ababcdcdababcdcd'))