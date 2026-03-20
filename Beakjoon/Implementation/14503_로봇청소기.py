import sys

# sys.stdin = open("input.txt", "r")

n,m = map(int,sys.stdin.readline().split())
r, c, d = map(int,sys.stdin.readline().split())
grid = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# 북(0),동(1),남(2),서(3)
dr = [-1,0,1,0]
dc = [0,1,0,-1]

cl_cnt = 0
while True:
    # 0 : 빈칸, 1 : 벽, 2 : 청소 완료 
    if grid[r][c] == 0:
        grid[r][c] = 2
        cl_cnt += 1
        
    # 주변 4칸에 빈칸이 있는지 확인
    has_blank = False
    for i in range(4):
        nr,nc = r + dr[i] , c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if grid[nr][nc] == 0:
                # 빈칸이 있으면
                has_blank = True 
                break

    # 빈칸이 없는 경우
    if not has_blank:
        back_dir = (d+2) % 4
        br,bc = r + dr[back_dir], c + dc[back_dir]

        if 0 <= br < n and 0 <= bc < m and grid[br][bc] != 1:
            r,c = br,bc
        else:
            break

    # 주변 4칸에 빈칸이 있는 경우
    else:
        d = (d+3) % 4
        nr, nc = r + dr[d] , c + dc[d]
        
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
            r,c = nr,nc
        
print(cl_cnt)
    