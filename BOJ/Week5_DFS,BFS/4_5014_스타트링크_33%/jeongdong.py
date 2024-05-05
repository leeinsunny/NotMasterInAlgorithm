# 5014 스타트링크
import sys
import collections

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = set()
queue = collections.deque()
count = 0

queue.append(S)

flag = False

while queue:
    for _ in range(len(queue)):
        now = queue.popleft()
        if now == G:
            flag = True
            break
        # 올라갈 때
        up_stair = now + U
        if 1 <= up_stair <= F and up_stair not in visited:
            queue.append(up_stair)
            visited.add(up_stair)
        # 내려갈 때
        down_stair = now - D
        if 1 <= down_stair <= F and down_stair not in visited:
            queue.append(down_stair)
            visited.add(down_stair)
    if flag:
        break
    count += 1

if flag:
    print(count)
else:
    print("use the stairs")
