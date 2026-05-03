"""
***로직 작성법***
로직은 크게 [입력 처리 - 핵심 변수 정의 - 로직 단계별 기술 - 예외 처리]
1. max_col, min_col, max_row, max_col 변수 설정
2. survey의 원소갯수만큼 step 작성
3. 각 step마다 점수를 딕셔너리 value값에 저장
4. 딕셔너리에 저장된 유형쌍에서 value값을 비교해 mbti를 확정
"""
from pprint import pprint
def solution(wallpaper):
    answer = []
    max_x ,max_y = 0,0
    min_x, min_y = 50,50
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                # x좌표(열) 처리
                if i < min_x: min_x = i
                if i > max_x: max_x = i
                
                # y좌표(행) 처리
                if j < min_y: min_y = j
                if j > max_y: max_y = j
                
    return [min_x,min_y,max_x+1, max_y+1]