import sys

input = sys.stdin.readline

N = int(input())

users = []
for i in range(N):
    age, name = input().strip().split()
    users.append((int(age), i, name))

for age, _, name in sorted(users):
    print(f'{age} {name}')