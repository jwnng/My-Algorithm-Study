import sys

# sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n+1)
count = 0

def bfs(now):
    global count
    visited[now] = True

    for next_com in adj[now]:
        if not visited[next_com]:
            count += 1
            bfs(next_com)

bfs(1)
print(count)
        