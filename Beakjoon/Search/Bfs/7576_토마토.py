import sys
from collections import deque
sys.stdin = open("input.txt","r")
m,n = map(int,sys.stdin.readline().split())
grid = [ list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]
queue = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            queue.append((i,j))
        
def Bfs():
    while queue:
        r,c = queue.popleft()

        for i in range(4):
            nr,nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == 0:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))

Bfs()

ans = 0
for row in grid:
    for tomato in row:
        if tomato == 0: 
           print(-1)
           exit()
        ans = max(ans,tomato)

print(ans-1)