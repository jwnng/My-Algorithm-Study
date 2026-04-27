"""
문제: 신규아이디추천 (Level_tests/Level_1)
난이도: Level 1

[오늘의 삽질 포인트]
1. 얕은 복사 문제:
   - 문자열을 새로운 문자열에 그대로 대입해서 사용하면 리스트 변수는 실제 데이터를 담고 있는 것이 아니라, 데이터가 있는 메모리 주소를 가리키기 때문에 
     기존의 문자열을 수정하면 새로운 문자열도 그대로 지워지는 문제가 발생함.
   - 해결: 깊은 복사를 이용해야함을 깨달음 1. 슬라이싱을 이용하여 2. list() 함수 이용 3. copy() 메서드 이용

[핵심 로직]
- 예외 처리: 각 단계마다 문자열(혹은 리스트)이 비어있을 수 있음을 인지하고, 인덱스 접근 전 반드시 **길이 체크(if not s)**를 수행해야 함.
- 연속 문자 처리: while '..' in s: s.replace('..', '.') 또는 스택을 활용하여 중복 문자를 효율적으로 제거.
- 양 끝 문자 제거: strip('.')을 활용하면 [0]이나 [-1] 인덱스 에러 걱정 없이 깔끔하게 앞뒤 마침표 제거 가능.
"""

def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    Lv2 = ""
    for char in new_id:
        if char.isalnum() or char in '-_.':
            Lv2 += char
        
    # 3단계
    while ".." in Lv2:
        Lv2 = Lv2.replace('..','.')

    # 4단계
    Lv4 = Lv2.strip('.')
    
    # 5단계
    if not Lv4:
        Lv4 = 'a'
        
    # 6단계
    if len(Lv4) >= 16:
        Lv4 = Lv4[:15].strip('.')

    # 7단계
    while len(Lv4) < 3:
        Lv4 += Lv4[-1]
    
    return Lv4

# print(solution("...!@BaT#*..y.abcdefghijklm"))
#print(solution("abcdefghijklmn.p"))
#print(solution("z-+.^."))
print(solution("aaa"))