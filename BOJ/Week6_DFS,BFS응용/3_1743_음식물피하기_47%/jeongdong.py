import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline
N, M, K = map(int, input().split())
visited = [[False] * M for _ in range(N)]
matrix = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    matrix[x - 1][y - 1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x, y):
    visited[x][y] = True
    global cnt
    cnt += 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
            if visited[nx][ny] is False and matrix[nx][ny] == 1:
                DFS(nx, ny)
    return cnt


result = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] is False and matrix[i][j] == 1:
            cnt = 0
            temp = DFS(i, j)
            result = max(result, temp)
print(result)
