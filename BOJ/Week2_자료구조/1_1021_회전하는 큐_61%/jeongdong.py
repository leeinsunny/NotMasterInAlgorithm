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
    global result
    target = dq.popleft()
    dq.append(target)
    result += 1


def goRight():
    global result
    target = dq.pop()
    dq.appendleft(target)
    result += 1


for num in findNumber_list:
    move = dq.index(num)
    if move == 0:
        dq.popleft()
        continue

    if move <= int(len(dq) / 2):
        for i in range(move):
            goLeft()
    else:
        for i in range(len(dq) - move):
            goRight()
    dq.popleft()
print(result)
