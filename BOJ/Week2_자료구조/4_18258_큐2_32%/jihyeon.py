from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
dq = deque()

for _ in range(n):
    command = input().rstrip().split()  
    cmd = command[0]

    if cmd == 'push':
        dq.append(command[1])
    elif cmd == 'pop':
        print(dq.popleft() if dq else -1)
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        print(0 if dq else 1)
    elif cmd == 'front':
        print(dq[0] if dq else -1)
    elif cmd == 'back':
        print(dq[-1] if dq else -1)
