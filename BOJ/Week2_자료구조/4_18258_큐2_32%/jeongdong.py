# 18258 큐2

import sys
from collections import deque

input = sys.stdin.readline
dq = deque()
command_list = ["push", "pop", "size", "empty", "front", "back"]
N = int(input())
for i in range(N):
    input_command = list(input().split())
    if input_command[0] == "push":
        dq.appendleft(input_command[1])
    elif input_command[0] == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif input_command[0] == "size":
        print(len(dq))
    elif input_command[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif input_command[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            target = dq.pop()
            print(target)
            dq.append(target)
    elif input_command[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            target = dq.popleft()
            print(target)
            dq.appendleft(target)

# chatGpt의 최적화 코드

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# def push(x, dq):
#     dq.appendleft(x)
#
# def pop(dq):
#     if not dq:
#         return -1
#     else:
#         return dq.pop()
#
# def size(dq):
#     return len(dq)
#
# def empty(dq):
#     return 1 if not dq else 0
#
# def front(dq):
#     return dq[-1] if dq else -1
#
# def back(dq):
#     return dq[0] if dq else -1
#
# # 명령에 대한 함수 매핑
# commands = {"push": push, "pop": pop, "size": size, "empty": empty, "front": front, "back": back}
#
# N = int(input())
# dq = deque()
#
# for _ in range(N):
#     input_command = input().split()
#     command = input_command[0]
#     if command == "push":
#         commands[command](input_command[1], dq)
#     else:
#         print(commands[command](dq))
