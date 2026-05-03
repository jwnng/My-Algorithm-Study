"""
***로직 작성법***
로직은 크게 [입력 처리 - 핵심 변수 정의 - 로직 단계별 기술 - 예외 처리]
1. mbti : 각 유형마다 점수를 저장하는 딕셔너리
2. survey의 원소갯수만큼 step 작성
3. 각 step마다 점수를 딕셔너리 value값에 저장
4. 딕셔너리에 저장된 유형쌍에서 value값을 비교해 mbti를 확정
"""
from collections import defaultdict
from pprint import pprint
def solution(survey, choices):
    answer = ''
    mbti = {
        'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0,'A' : 0, 'N' : 0
    }
    for type,score in zip(survey,choices):
        t1,t2 = list(type)
        if score < 4:
            mbti[t1] += 4-score
        elif score > 4:
            mbti[t2] += score-4
    
    if mbti['R'] >= mbti['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if mbti['C'] >= mbti['F']:
        answer += 'C'
    else:
        answer += 'F'
    if mbti['J'] >= mbti['M']:
        answer += 'J'
    else:
        answer += 'M'
    if mbti['A'] >= mbti['N']:
        answer += 'A'
    else:
        answer += 'N'
         
        
    return answer