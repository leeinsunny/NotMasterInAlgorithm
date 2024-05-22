import sys
input = sys.stdin.readline

arr = [0] * 101 
arr[1], arr[2], arr[3] = 1, 1, 1
for i in range(4, 101):
    arr[i] = arr[i-2] + arr[i-3]

T = int(input())
for _ in range(T):
    N = int(input())
    print(arr[N])