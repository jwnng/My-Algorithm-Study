"""
***로직***
1. 핵심 변수
- stack: 가격이 떨어지지 않은 시점의 인덱스를 담는 통
- answer: 각 시점별로 가격이 유지된 시간을 담은 배열 (처음엔 최대 시간으로 초기화)
2. 핵심 로직
Step 1: 순회 및 비교
- prices를 하나씩 확인하면서, 현재 가격이 스택 맨 위에 있는 인덱스의 가격보다 낮은지 확인한다.
Step 2: 스택 털기 (가격 하락 발생)
- 현재 가격이 더 낮다면(가격 하락), 스택에서 인덱스를 꺼내고 현재 인덱스 - 꺼낸 인덱스를 계산해 유지 시간을 확정한다.
Step 3: 마무리
- 끝까지 순회한 후에도 스택에 남은 인덱스들은 끝까지 가격이 안 떨어진 것들이다. 전체 길이에서 각 인덱스를 빼서 남은 시간을 계산한다.4. 예외처리
4. 예외 처리
- prices = 100,000 일 때 이중 for문 --> 100억번. 보통 코테는 1억번까지가 한계이기 때문에 탈락
- 가격이 떨어지는 시점도 계산을 해줘야 함
"""
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [] # 인덱스를 저장할 스택

    for i in range(n):
        # 가격이 떨어졌다면 스택에서 꺼내서 시간 확정
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # 끝까지 가격이 떨어지지 않은 인덱스들 처리
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer


"""
*** 실패 코드 ***
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        p = prices.popleft()
        sec = 0
        for next in prices:
            if p <= next:
                sec += 1
        answer.append(sec)
        
    return answer"""