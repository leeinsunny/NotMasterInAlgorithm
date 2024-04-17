# 9461 파도반수열
import sys

input = sys.stdin.readline

T = int(input())

dp = [0] * 101


def dpFunc(x):
    if x <= 3:
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = dpFunc(x - 2) + dpFunc(x - 3)
    return dp[x]


for _ in range(T):
    print(dpFunc(int(input())))
