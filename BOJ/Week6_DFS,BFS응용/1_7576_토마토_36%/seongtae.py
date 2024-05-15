import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def bfs(coords):
    days = 0
    for coord in coords:
        coord.append(days)
    queue = deque(coords)

    while queue:
        x, y, current_day = queue.popleft()
        days = current_day

        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < N and 0 <= next_y < M and grid[next_x][next_y] == 0:
                grid[next_x][next_y] = 1
                queue.append([next_x, next_y, current_day + 1])

    return days

    

def solution():
    total_tomato = 0
    start_coords = []

    for x in range(N):
        for y in range(M):
            if grid[x][y] != -1:
                total_tomato += 1
            if grid[x][y] == 1:
                start_coords.append([x, y])

    days = bfs(start_coords)

    for x in range(N):
        for y in range(M):
            if grid[x][y] == 0:
                return print(-1)

    print(days)

solution()

