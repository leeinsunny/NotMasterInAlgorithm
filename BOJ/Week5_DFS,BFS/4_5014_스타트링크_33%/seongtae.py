#5014 스타트링크
import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())


visited = set([S])
queue = deque([(S, 0)])
min_count = None

while queue:
    floor, count = queue.popleft()

    if floor == G:
        if min_count is not None:
            min_count = min(min_count, count)
        else:
            min_count = count

    lower_floor, higher_floor = floor - D, floor + U

    if lower_floor >= 1 and lower_floor not in visited:
        queue.append((lower_floor, count + 1))
        visited.add(lower_floor)

    if higher_floor <= F and higher_floor not in visited:
        queue.append((higher_floor, count + 1))
        visited.add(higher_floor)

if min_count is None:
    print("use the stairs")
else:
    print(min_count)

