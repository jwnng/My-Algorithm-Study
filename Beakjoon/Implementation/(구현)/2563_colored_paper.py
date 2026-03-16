n = int(input())

MAX_R = 1000

grid = [[ 0 for i in range(MAX_R)] for j in range(MAX_R)]
s = 0

for _ in range(n):
    x,y = map(int,input().split())

    for i in range(y+1,y + 11):
        for j in range(x+1,x + 11):
            if grid[i][j] == 1:
                continue
            grid[i][j] = 1
            s += 1
        
print(s)