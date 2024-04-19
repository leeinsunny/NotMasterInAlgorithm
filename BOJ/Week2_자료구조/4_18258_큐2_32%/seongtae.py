import sys
import collections

input = sys.stdin.readline

N = int(input())

queue = collections.deque()

for _ in range(N):
    args = input().strip().split()

    operation = args[0]

    if operation == 'push':
        item = int(args[1])
        queue.append(item)
    elif operation == 'pop':
        print(queue.popleft() if queue else -1)
    elif operation == 'size':
        print(len(queue))
    elif operation == 'empty':
        print(0 if queue else 1)
    elif operation == 'front':
        print(queue[0] if queue else -1)
    elif operation == 'back':
        print(queue[-1] if queue else -1)
    