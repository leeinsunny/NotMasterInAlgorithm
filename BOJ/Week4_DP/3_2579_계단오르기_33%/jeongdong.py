# 2579 계단오르기
import sys

input = sys.stdin.readline

N = int(input())
stair = [0]
for i in range(N):
    stair.append(int(input()))
matrix = [[0] * 3 for i in range(N + 1)]

for i in range(1, N + 1):
    matrix[i][0] = max(matrix[i - 1][1], matrix[i - 1][2])
    matrix[i][1] = matrix[i - 1][2] + stair[i]
    matrix[i][2] = matrix[i - 1][0] + stair[i]

print(max(matrix[N][1], matrix[N][2]))
