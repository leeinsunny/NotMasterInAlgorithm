import sys

input = sys.stdin.readline

N = int(input())

grid = [
    [num for num in map(int, input().split())]
    for _ in range(N)
]

def has_single_color(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if grid[i][j] != grid[x][y]:
                return False
    return True

def dfs(x, y, size):
    if has_single_color(x, y, size):
        return [1, 0] if grid[x][y] == 0 else [0, 1]
    
    counts = [0, 0]
    half_size = size // 2
    for dx, dy in [(0, 0), (half_size, 0), (0, half_size), (half_size, half_size)]:
        white_count, blue_count = dfs(x + dx, y + dy, half_size)
        counts[0] += white_count
        counts[1] += blue_count

    return counts


white_count, blue_count = dfs(0, 0, N)

print(white_count)
print(blue_count)