# 15650 N과 M

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_list = [i for i in range(1, N + 1)]
# [1,2,3]
answer = []


def dfs(start_index, sub_list):
    if len(sub_list) == M:
        answer.append(sub_list[:])
        return
    for i in range(start_index, len(num_list)):
        dfs(i + 1, sub_list + [num_list[i]])


dfs(0, [])
for e in answer:
    print(*e)
