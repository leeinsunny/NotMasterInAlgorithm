# 1021 회전하는 큐
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
findNumber_list = list(map(int, input().split()))

dq = deque()
for i in range(1, N + 1):
    dq.append(i)
result = 0


def goLeft():
    target = dq.popleft()
    dq.append(target)


def goRight():
    target = dq.pop()
    dq.appendleft(target)


for num in findNumber_list:
    move = dq.index(num)
    if move == 0:
        dq.popleft()
        continue

    if move <= int(len(dq) / 2):
        for i in range(move):
            goLeft()
            result += 1
    else:
        for i in range(len(dq) - move):
            goRight()
            result += 1
    dq.popleft()
print(result)
