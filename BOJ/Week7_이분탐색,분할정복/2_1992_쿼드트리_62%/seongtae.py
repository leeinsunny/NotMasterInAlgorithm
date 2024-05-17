import sys

input = sys.stdin.readline

N = int(input())

grid = [
    [char for char in input().strip()]
    for _ in range(N)
]

def has_single_color(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if grid[i][j] != grid[x][y]:
                return False
    return True

def compress(x, y, size):
    if has_single_color(x, y, size):
        return grid[x][y]
    
    result = '('
    half_size = size // 2
    for dx, dy in [(0, 0), (0, half_size), (half_size, 0), (half_size, half_size)]:
        result += compress(x + dx, y + dy, half_size)
    result += ')'

    return result

print(compress(0, 0, N))