# 10870 피보나치수 5
import sys

value = int(sys.stdin.readline())


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(value))
