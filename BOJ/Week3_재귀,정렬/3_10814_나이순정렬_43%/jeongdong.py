# #10814 나이순 정렬
import sys

input = sys.stdin.readline

N = int(input())

result_list = []
for i in range(N):
    info = input().split()
    age = int(info[0])
    name = info[1]
    result_list.append([age, name])
result_list.sort(key=lambda x : x[0])
for e in result_list:
    print(*e)