"""
***로직 작성법***
로직은 크게 [입력 처리 - 핵심 변수 정의 - 로직 단계별 기술 - 예외 처리]
1. n: 진법(2-16), t: 내가 출력해야하는 숫자의 개수, m: 게임에 참가하는 인원, p: 나의 순서
2.  full_s: 모든 숫자를 진수 변환하여 한 글자씩 이어 붙인 전체 문자열
    num: 0부터 시작하여 1씩 증가되어 변환되는 10진수 숫자
    answer: 순서에 맞게 글자들을 모아둔 결과값
3.  step1: 진법 변환 함수 구현
        - 10진수 num을 n진수로 변환한다.
        - num을 n으로 나눈 나머지를 digits 인덱스에서 찾아 결과 앞에 붙이고, 몫을 갱신하는 과정을 반복한다.
        - 예외처리: 0일 경우 바로 "0"을 반환 
    step2: 전체 문자열 생성
        - 게임이 끝날 때까지 필요한 글자 개수는 t*m
        - full_s의 길이가 t*m 보다 작을 경우 0부터 1까지 증가시키며 n진수로 변환하여 full_s에 이어붙인다
    step3: 본인 차례 글자 추출
        - full_s에서 나의 첫번째 순서인 p-1부터 시작하여 m씩 증가시키며 
          answer의 갯수가 t개가 될때따지 answer에 이어붙인다
"""

def decimal_to_n(num, base):
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEF"
    result = ""
    
    while num > 0:
        remainder = num % base
        result = digits[remainder] + result
        num = num // base
    return result

def solution(n, t, m, p):
    full_s = ""
    l = t*m+1
    num = 0
    while len(full_s) < (t*m):
        full_s += decimal_to_n(num,n)
        num += 1
        
    answer = ""
    for i in range(t):
        idx = (p-1) + (i*m)
        answer += full_s[idx]
        
    return answer