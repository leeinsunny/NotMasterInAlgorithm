from collections import deque

# 미로의 크기 입력받기
N, M = map(int, input().split())

# 미로 정보 입력받기
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

# 미로 문제를 풀 때는 이동할 수 있는 경우의 수를 표현해주기
# 상,하,좌,우 정의
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def BFS(x, y):
    queue = deque()
    queue.append((x,y)) #시작점을 큐에 넣기

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 이동할 수 있는 모든 방향을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로의 크기를 벗어나면 안되므로 조건 추가
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            # 0인 칸으로는 이동할 수 없다는 조건 추가
            if graph[nx][ny]==0:
                continue
            # 1인 칸은 이동할 수 있으므로 진행
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    # 마지막 값에서 카운트 값 뽑기
    return graph[N-1][M-1]

print(BFS(0,0))