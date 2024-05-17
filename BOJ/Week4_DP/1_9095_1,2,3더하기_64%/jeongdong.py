# 9095 1,2,3더하기
import sys

input = sys.stdin.readline

T = int(input())
dp = [0] * 11


def dpFunc(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    if dp[x] != 0:
        return dp[x]
    dp[x] = dpFunc(x - 3) + dpFunc(x - 2) + dpFunc(x - 1)
    return dp[x]


for _ in range(T):
    print(dpFunc(int(input())))
