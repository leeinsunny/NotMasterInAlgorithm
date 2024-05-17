import sys
import collections

input = sys.stdin.readline

M, N = map(int, input().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = collections.deque()

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append((i, j))

cnt = 0
while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                if matrix[nx][ny] == 0:
                    queue.append((nx, ny))
                    matrix[nx][ny] = 1
    cnt += 1

flag = True

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            flag = False

if flag:
    print(cnt - 1)
else:
    print(-1)
