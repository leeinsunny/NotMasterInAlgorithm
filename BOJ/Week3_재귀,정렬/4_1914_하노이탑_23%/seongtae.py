import sys
N = int(sys.stdin.readline())

def hannoi_moves(n, base, temp, target, moves):
    for i in range(n - 1, 0, -1):
        hannoi_moves(i, base, target, temp, moves)
        moves.append((base, target))
        base, temp = temp, base
    
    moves.append((base, target))
    return moves

def hannoi_count(n, memo):
    if n in memo:
        return memo[n]
        
    count = 1
    for i in range(n - 1, 0, -1):
        count += hannoi_count(i, memo) + 1

    memo[n] = count
    return count
    
    
if N <= 20:
    moves = hannoi_moves(N, 1, 2, 3, [])
    print(len(moves))
    for i, j in moves:
        print(f'{i} {j}')
else:
    print(hannoi_count(N, {}))
    
