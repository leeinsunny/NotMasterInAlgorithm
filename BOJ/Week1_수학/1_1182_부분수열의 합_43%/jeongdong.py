# 1182 부분수열의 합
import sys
from itertools import combinations

input = sys.stdin.readline
cnt = 0
N, S = map(int, input().split())
num_list = list(map(int, input().split()))


for i in range(1, N + 1):
    combi = list(combinations(num_list, i))
    for e in combi:
        if sum(e) == S:
            cnt += 1
print(cnt)


# chatGPT로 검색한 해결법

# def subsets(nums):
#     def backtrack(start, path):
#         # 현재 경로를 결과에 추가
#         result.append(path[:])
#         # 각 요소에 대해 하위 부분집합 찾기
#         for i in range(start, len(nums)):
#             # 요소를 경로에 추가
#             path.append(nums[i])
#             # 다음 요소로 이동하고 재귀적으로 탐색
#             backtrack(i + 1, path)
#             # 경로에서 요소 제거 (백트래킹)
#             path.pop()
#
#     result = []
#     backtrack(0, [])
#     return result
#
#
# result_list = subsets(num_list)
# for e in result_list:
#     if sum(e) == S:
#         cnt += 1
# print(cnt)
