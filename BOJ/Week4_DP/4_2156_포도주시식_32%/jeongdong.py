# 2156 포도주 시식
import sys

input = sys.stdin.readline

N = int(input())
wine = [0]
for _ in range(N):
    wine.append(int(input()))

matrix = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    matrix[i][0] = max(matrix[i - 1][0], matrix[i - 1][1], matrix[i - 1][2])
    matrix[i][1] = matrix[i - 1][2] + wine[i]
    matrix[i][2] = matrix[i - 1][0] + wine[i]

print(max(matrix[N][0], matrix[N][1], matrix[N][2]))
