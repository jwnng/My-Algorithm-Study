def solution(t, p):
    answer = 0
    for i in range(0,len(t)):
        if len(t[i:i+len(p)]) == len(p) and int(t[i:i+len(p)]) <= int(p):
            answer += 1
            
    return answer
    
"""
*** 더 파이써닉한 코드***
def solution(t, p):
    p_len = len(p)
    p_num = int(p)
    
    # 반복문 범위 자체를 짤릴 일 없는 안전한 구간까지만 돌립니다.
    return sum(1 for i in range(len(t) - p_len + 1) if int(t[i:i+p_len]) <= p_num)
    
"""