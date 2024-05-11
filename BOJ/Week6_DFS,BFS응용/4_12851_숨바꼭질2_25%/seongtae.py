import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())


min_seconds_by_point = defaultdict(lambda : 200000)
queue = deque([(N, 0)])
count = 0

while queue:
    point, seconds = queue.popleft()

    if point == K:
        if seconds == min_seconds_by_point[point]:
            count += 1
        elif seconds < min_seconds_by_point[point]:
            count = 1
    
    min_seconds_by_point[point] = min(min_seconds_by_point[point], seconds)

    for diff in [-1, 1, point]:
        next_point = point + diff
        next_seconds = seconds + 1

        if next_seconds > min(min_seconds_by_point[K], min_seconds_by_point[next_point]):
            continue

        if 0 <= next_point <= 200000:
            queue.append((next_point, next_seconds))

print(min_seconds_by_point[K])
print(count)


        

    

    