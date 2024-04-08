import sys
from collections import deque

# 입력값을 받는다.
size, num = map(int, input().split())
idx = list(map(int, input().split()))

# 큐를 생성한다.
queue = deque([i for i in range(1, size+1)])
count = 0

for i in idx:
    while True:
        # 찾으려는 인덱스와 현재 큐의 맨 앞에 있는 원소가 일치할 때까지 반복한다.
        if i == queue[0]:
            queue.popleft()  # 원하는 인덱스를 찾았으므로 큐에서 제거한다.
            break

        # 찾으려는 인덱스의 위치가 중간보다 앞에 있으면 앞에서부터 찾는다.
        if queue.index(i) <= len(queue) // 2:
            while i != queue[0]:
                queue.append(queue.popleft())  # 맨 앞의 원소를 맨 뒤로 이동시킨다.
                count += 1

        # 찾으려는 인덱스의 위치가 중간보다 뒤에 있으면 뒤에서부터 찾는다.
        else:
            while i != queue[0]:
                queue.appendleft(queue.pop())  # 맨 뒤의 원소를 맨 앞으로 이동시킨다.
                count += 1

print(count)