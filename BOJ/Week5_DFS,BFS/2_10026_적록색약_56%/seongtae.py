#10026 적록색약
import sys
from collections import deque 

input = sys.stdin.readline

N = int(input())

grid = [
    [ color for color in input().strip() ]
    for _ in range(N)
]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def bfs_normal(x, y, visited):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < N and 0 <= next_y < N and grid[next_x][next_y] == grid[x][y] and (next_x, next_y) not in visited:
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
            
def bfs_blind(x, y, visited):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < N and 0 <= next_y < N and \
                (next_x, next_y) not in visited and \
                ( \
                    grid[next_x][next_y] == grid[x][y] or \
                    (grid[next_x][next_y], grid[x][y]) in [('R', 'G'), ('G', 'R')] \
                ) :
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
            
visited_normal = set()
visited_blind = set()
count_normal = 0
count_blind = 0

for x in range(N):
    for y in range(N):
        if (x, y) not in visited_normal:
            bfs_normal(x, y, visited_normal)
            count_normal += 1
        
        if (x, y) not in visited_blind:
            bfs_blind(x, y, visited_blind)
            count_blind += 1

print(f'{count_normal} {count_blind}')



