import sys

N = int(sys.stdin.readline())

def calc_fibonacci(n):
    memo = [None] * (n + 1)

    def fib(n):
        if n <= 1:
            return n
        
        if memo[n] is not None:
            return memo[n]

        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]
    
    return fib(n)

print(calc_fibonacci(N))
