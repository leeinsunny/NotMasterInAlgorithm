import sys
N = int(sys.stdin.readline())

moves = []

def hannoi(n, base, temp, target):
    for i in range(n - 1, 0, -1):
        hannoi(i, base, target, temp)
        moves.append((base, target))
        base, temp = temp, base
    
    moves.append((base, target))

hannoi(N, 1, 2, 3)

print(len(moves))
for i, j in moves:
    print(f'{i} {j}')