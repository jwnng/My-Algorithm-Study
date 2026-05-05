"""
***로직***
1. 입력 변수: 
    s: 전체 문자열
2. 핵심 변수
    prev: 뒤 문자열과 비교할 기준 문자열
    compress: 전체 문자열을 압축한 문자열
    count: 같은 문자열을 새는 변수
3. 핵심 로직        
step1: 문자열 압축
- 비교할 기준 문자열을 1개부터 문자열의 절반까지 1개씩 증가시킬 step변수 생성
step2: 문자열 비교
- step변수를 기준으로 현재 문자열은 step부터 전체 문자열 갯수까지 step단위로 비교할 curr 변수 생성하여 prev문자열과 비교함
- prev == curr이라면 count를 1씩 증가시키고 다를 때는 prev를 curr로 초기화함
step3: 문자열 완성
- 현재 문자열이 이전 문자열과 같다면 갯수를 카운트하여 compress 빈 문자열에 (숫자+문자열)로, 이전과 같지 않다면 문자열만 + 연산을 함
step4:
- 압축할 문자열 갯수를 기준으로 완성한 문자열의 갯수를 answer에 저장해서 갯수가 더 짧은 문자열이 있다면 초기화
- 반복문이 끝난 후, 마지막으로 비교 중이던 prev와 count를 compress에 추가
4. 예외 처리
- 문자열이 1 이하일 경우 예외 처리
"""
def solution(s):
    if len(s) == 1:
        return 1
    
    answer = len(s)
    
    for step in range(1,len(s)//2+1):
        prev = s[0:step] 
        compress = ""
        count = 1
        for j in range(step,len(s),step):
            curr = s[j:j+step]
            
            if curr == prev:
                count += 1
            else:    
                compress += (str(count) + prev) if count >= 2 else prev
                prev = curr
                count = 1
                
        compress += (str(count) + prev) if count >= 2 else prev
    
        answer = min(len(compress),answer)
    return answer
print(solution("aabbaccc"))