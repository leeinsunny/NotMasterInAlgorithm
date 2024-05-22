from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())  
targets = list(map(int, input().split())) 
dq = deque(range(1, n + 1)) 

count = 0 
for t in targets:
    pos = dq.index(t) 
    if pos < len(dq) / 2:
        while dq[0] != t:
            dq.rotate(-1)
            count += 1
    else:
        while dq[0] != t:
            dq.rotate(1)
            count += 1
    dq.popleft()

print(count)
