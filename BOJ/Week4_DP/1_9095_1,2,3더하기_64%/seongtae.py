import sys

T = int(sys.stdin.readline())

test_cases = [
    int(sys.stdin.readline()) for _ in range(T)
]

memo = [0] * 11

def paths(n):
    if memo[n]:
        return memo[n]
    
    if n <= 1:
        return 1
    elif n <= 2:
        return 2
    elif n <= 3:
        return 4
    
    return paths(n-1) + paths(n-2) + paths(n-3)

for test in test_cases:
    print(paths(test))