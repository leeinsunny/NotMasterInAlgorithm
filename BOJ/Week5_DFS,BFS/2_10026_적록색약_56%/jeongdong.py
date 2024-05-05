# 10026 적록색약
import sys
import collections

input = sys.stdin.readline

N = int(input())
matrix = []

# 방문 배열
visited = [[False for _ in range(N)] for _ in range(N)]

# 움직임
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 배열에 넣기
for _ in range(N):
    matrix.append(list(input().rstrip()))


# 너비 우선 탐색
def BFS(x, y, color):
    queue = collections.deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        now = queue.popleft()
        x = now[0]
        y = now[1]

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and matrix[nx][ny] == color:
                    queue.append([nx, ny])
                    visited[nx][ny] = True


# 정상
def normal():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                color = matrix[i][j]
                BFS(i, j, color)
                cnt += 1
    return cnt


# 적록색약
def color_blindness():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'R':
                matrix[i][j] = 'G'

    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                color = matrix[i][j]
                BFS(i, j, color)
                cnt += 1
    return cnt


print(normal(), end=" ")
visited = [[False for _ in range(N)] for _ in range(N)]
print(color_blindness())
