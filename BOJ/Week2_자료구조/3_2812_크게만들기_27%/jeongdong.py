# 2812 크게 만들기
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
number_list = list(input().strip())
stack = []

for num in number_list:
    while K > 0 and stack and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)
if K > 0:
    stack = stack[:-K]

print(str().join(stack))
