"""
***로직***
1. 입력 변수
- cacheSize: 캐시 크기
- cities: 도시 이름을 담은 배열
2. 핵심 변수
- cache: 캐시 처리를 위한 덱
3. 핵심 로직
step1: 캐시 배열 생성
- 캐시 처리를 위한 덱 변수 생성
step2: 캐시 처리
- 도시 배열 요소를 순서대로 돌면서 캐시 안에 도시가 있다면 캐시 히트 처리를, 없다면 캐시 미스 처리를 하며 시간 측정을 함
4. 예외 처리
- 캐시 사이즈가 0이라면 캐시 미스 처리를 미스 처리 시간 * 도시 배열 요소 갯수로 바로 처리
"""
# 캐시 크기에 따른 실행시간 측정 프로그램
# 총 실행시간 출력
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for c in cities:
        c = c.lower()
        if c in cache:
            answer += 1
            cache.remove(c)
            cache.append(c)
        
        else:
            answer += 5
            if len(cache) != cacheSize:
                cache.append(c)    
            else:
                cache.popleft()
                cache.append(c)
    return answer