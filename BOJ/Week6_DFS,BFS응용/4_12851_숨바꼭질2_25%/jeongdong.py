import sys
import collections

input = sys.stdin.readline
road = [0] * 100001

queue = collections.deque()
N, K = map(int, input().split())


cnt = 0
check = 0
queue.append(N)

while queue:
    x = queue.popleft()
    if x == K:
        cnt = road[x]
        check += 1

    if 0 <= x - 1 <= 100000:
        if road[x - 1] == 0 or road[x - 1] == road[x] + 1:
            road[x - 1] = road[x] + 1
            queue.append(x - 1)

    if 0 <= x + 1 <= 100000:
        if road[x + 1] == 0 or road[x + 1] == road[x] + 1:
            road[x + 1] = road[x] + 1
            queue.append(x + 1)

    if 0 <= 2 * x <= 100000:
        if road[2 * x] == 0 or road[2 * x] == road[x] + 1:
            road[2 * x] = road[x] + 1
            queue.append(2 * x)

print(cnt)
print(check)
