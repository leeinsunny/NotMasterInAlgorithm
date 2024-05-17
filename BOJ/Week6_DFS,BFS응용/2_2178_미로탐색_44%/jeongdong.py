import sys
import collections

input = sys.stdin.readline
N, M = map(int, input().split())
matrix = []
visited = [[False] * M for i in range(N)]
for _ in range(N):
    matrix.append(list(input().rstrip()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = collections.deque()

queue.append((0, 0))
visited[0][0] = True
count = 1
flag = False

while queue:
    size = len(queue)
    for _ in range(size):
        x, y = queue.popleft()
        if x == N - 1 and y == M - 1:
            flag = True
            break
        for i in range(len(dx)):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                if visited[nx][ny] is False and matrix[nx][ny] == '1':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    if flag:
        break
    count += 1

print(count)
