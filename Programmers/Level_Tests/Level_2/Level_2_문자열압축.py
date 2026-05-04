"""
***로직***
1. 입력 변수: 
    
2. 핵심 변수
3. 핵심 로직

fo문으로만 하면 먼저 단어의 갯수를 지정하는 for문
        
- step1: 
- step2:
- step3: 

4. 예외 처리
- 문자열이 1 이하일 경우 예외 처리
"""
def solution(s):
    if len(s) == 1:
        return 1
    
    answer = len(s)
    
    for step in range(1,len(s)//2+1):
        compressed = ""
        prev = s[0:step] # 첫 번째 조각
        count = 1
        
        for j in range(step,len(s),step):
            curr = s[j:j+step] 
            
            if prev == curr:
                count += 1
            else:
                compressed += (str(count) + prev) if count >= 2 else prev
                prev = curr
                count = 1
                
        compressed += (str(count) + prev) if count >= 2 else prev
        
        answer = min(answer,len(compressed))
    return answer
