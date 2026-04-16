from collections import deque
def solution(priorities, location):
    answer = 0
    Q = deque([(p,i) for i,p in enumerate(priorities)])
    
    while Q:
        cur = Q.popleft()

        if any(cur[0] < next[0] for next in Q):
            Q.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                return answer