import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

waste_coords = set()

for _ in range(K):
    i, j = map(int, input().split())
    waste_coords.add((i - 1, j - 1))


dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def bfs(start_coord, visited):
    visited.add(start_coord)
    queue = deque([start_coord])
    size = 0

    while queue:
        x, y = queue.popleft()
        size += 1

        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy
            next_coord = (next_x, next_y)
            if 0 <= next_x < N and 0 <= next_y < M and next_coord in waste_coords and next_coord not in visited:
                visited.add(next_coord)
                queue.append(next_coord)
    return size


max_size = 0
visited = set()

for x in range(N):
    for y in range(M):
        coord = (x, y)
        if coord in waste_coords:
            size = bfs(coord, visited)
            max_size = max(max_size, size)

print(max_size)