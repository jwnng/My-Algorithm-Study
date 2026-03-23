import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().split())
grid = [[ list(map(int,sys.stdin.readline().strip())) ] for _ in range(n)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def bfs(start_r,start_c):
    