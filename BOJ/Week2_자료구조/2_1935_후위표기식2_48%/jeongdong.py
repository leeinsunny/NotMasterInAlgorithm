# 1935 후위표기식
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
expression = list(input().strip())
value_list = list()

for i in range(N):
    value_list.append(input().strip())


def strToInt(target):
    if 'A' <= target <= 'Z':
        target = str(value_list[ord(target) - ord('A')])
    return str(target)


dq = deque()

for e in expression:
    if 'A' <= str(e) <= 'Z':
        dq.append(e)
    else:
        target1 = strToInt(dq.pop())
        target2 = strToInt(dq.pop())
        dq.append(str(eval(target2 + e + target1)))
print(f'{float(dq.pop()):0.2f}')
