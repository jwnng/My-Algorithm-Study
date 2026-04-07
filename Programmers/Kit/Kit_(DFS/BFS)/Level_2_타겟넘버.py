def solution(numbers, target):

    def dfs(cur_n,depth):
        if depth == len(numbers):
            if cur_n == target:
                return 1
            else:
                return 0
            
        return dfs(cur_n + numbers[depth],depth + 1) + dfs(cur_n - numbers[depth],depth + 1)
        
    return dfs(0,0)

"""
from itertools import product
def solution(numbers, target):
    l = [ (x,-x) for x in numbers]
    s = [list(map(sum,product(*l)))]

    return s.count(target)
"""