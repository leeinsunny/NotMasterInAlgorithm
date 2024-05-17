#1914 하노이탑
N = int(input())
cnt = 0
result_list = []


def move(target, start, end):
    global cnt
    cnt += 1
    result_list.append([start, end])


# hanoi(N:개수,start:1, via:2, end:3)
def hanoi(N, one, two, three):
    if N == 1:
        move(N, one, three)
        return
    hanoi(N - 1, one, three, two)
    move(N, one, three)
    hanoi(N - 1, two, one, three)


if N > 20:
    print(2**N-1)
else:
    hanoi(N, 1, 2, 3)
    print(cnt)
    for e in result_list:
        print(*e)
