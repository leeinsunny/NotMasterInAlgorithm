# 1929 소수구하기
import sys

input = sys.stdin.readline


def getPrimes(start, end):
    Primes = [False, False] + [True] * (end - 1)

    p = 2
    while p * p <= end:
        if Primes[p]:
            for i in range(p * p, end + 1, p):
                Primes[i] = False
        p += 1
    return [i for i in range(start, end + 1) if Primes[i]]


M, N = map(int, input().split())
prime_list = getPrimes(M, N)
for i in prime_list:
    print(i)
