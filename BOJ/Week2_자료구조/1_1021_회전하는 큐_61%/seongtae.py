import sys

N, M = map(int, sys.stdin.readline().split())

queue = [True] * N
total_count = 0
head = 0

def find_index(target):
    count = 0
    for i in range(head, head + N):
        num = i % N
        if not queue[num]:
            continue

        if num == target:
            return count
        count += 1

def find_index_reverse(target):
    count = 0
    for i in range(head, head - N, -1):
        num = i if i >= 0 else i + N
        if not queue[num]:
            continue

        if num == target:
            return count
        count += 1


def find_next_valid_num(start):
    for i in range(start, start + N):
        num = i % N
        if queue[num]:
            return num


for i in list(map(int, sys.stdin.readline().split())):
    num = i - 1

    min_count = N
    min_count = min(min_count, find_index(num))
    min_count = min(min_count, find_index_reverse(num))

    queue[num] = False
    head = find_next_valid_num(num)
    total_count += min_count

print(total_count)