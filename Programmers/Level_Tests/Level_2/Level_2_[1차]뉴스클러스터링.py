import math
from collections import Counter
def solution(str1, str2):
    answer = 0
    # 자카드 유사도: 교집합의 합 / 합집합의 합
    # 1. 길이 2 이상인 두 문자열이 입력으로 주어짐, 입력 시에 그냥 소문자로 바꿔처리함.
    str1,str2 = str1.upper(),str2.upper()
    
    # 2. 압력으로 들어온 문자열은 두 글자씩 끊어서 다중 집합의 원소로 만든다.
    # 3. 영문자로 된 글자쌍만 유효하고, 기타 공백, 숫자,특수 문자가 포함되면 버림
    A_set = []
    prev_a = str1[0]
    
    for i in range(1,len(str1)):
        if prev_a.isalpha() and str1[i].isalpha():
            A_set.append((prev_a,str1[i]))
        prev_a = str1[i] 
    
    B_set = []
    prev_b = str2[0]
    for i in range(1,len(str2)):
        if prev_b.isalpha() and str2[i].isalpha():
            B_set.append((prev_b,str2[i]))
        prev_b = str2[i] 
    
    # 두 문자열 사이의 유사도를 계산하여 자카드 유사도를 출력
    A = Counter(A_set)
    B = Counter(B_set)
    
    intersection = list((A & B).elements())
    union = list((A | B).elements())
    
    # 예외 처리: 모두 공집합일 경우 나눗셈이 정의되지않으니 j(A,B) = 65536
    
    if not union:
        answer = 65536
    else:
        answer = len(intersection) / len(union) * 65536
    
    return math.floor(answer)