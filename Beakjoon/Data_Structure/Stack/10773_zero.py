import sys

# sys.stdin = open("input.txt", "r")
K = int(sys.stdin.readline())
list = []

for _ in range(K):
    n = int(input())
    
    if n != 0:
        list.append(n)    
    else:
            list.pop()
        
        
sys.stdout.write(str(sum(list)))