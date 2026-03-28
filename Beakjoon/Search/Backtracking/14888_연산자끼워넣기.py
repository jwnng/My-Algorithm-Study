import sys

sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
arr1 = [map(int,sys.stdin.readline().split())]
arr2 = []
op = [map(int,sys.stdin.readline().split())]
ans = []
result = 0

for x in arr1:
    arr2.append(x)
    arr2.append(0)

def solve(depth):
    