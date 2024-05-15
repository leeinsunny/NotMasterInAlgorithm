import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maze = [
    [int(char) for char in input().strip()]
    for _ in range(N)
]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def bfs(start_coord):
    visited = set([tuple(start_coord)])
    start_coord.append(1)
    queue = deque([start_coord])

    while queue:
        x, y, steps = queue.popleft()
        if x == N - 1 and y == M - 1:
            return steps

        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy
            next_coord = (next_x, next_y)
            if 0 <= next_x < N and 0 <= next_y < M and maze[next_x][next_y] == 1 and next_coord not in visited:
                visited.add(next_coord)
                queue.append([next_x, next_y, steps + 1])

min_steps = bfs([0, 0])
print(min_steps)

