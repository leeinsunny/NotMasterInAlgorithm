from collections import deque

#bfs 정의
def bfs():
  while queue:
    #익은 토마토 좌표를 하나씩 가져옴
    x,y = queue.popleft()
    #상하좌우 행과 열 변위
    dx = [-1,1,0,0]     # 행의 변위 ( 위 아래로 이동시에만 변함)
    dy = [0,0,-1,1]     # 열의 변위 ( 왼 오 이동시에만 변함)
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 상하좌우에 익지 않은 토마토(0)가 있으면 1을 더해 몇 번째인지 세주고
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y] + 1
          queue.append((nx, ny)) # 큐에 새로운 토마토 위치 추가

#입력받기
M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]


#익은 토마토 위치 quequ에 추가
queue = deque()
for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      queue.append([i,j])


# BFS; 토마토 익히기 시작
bfs()

# bfs 종료 후
day = 0
for row in graph:
    for i in row:
        if i == 0:  # 익지 않은 토마토가 있으면(=토마토가 모두 익지 못하는 상황) -1 출력
            print(-1)
            exit() # 다음 행의 여부와 관계 없이 -1만 출력해야하므로 종료시킴
    else: # 그래프에서 가장 큰 값이 마지막으로 익은 토마토임 → 한 줄씩 최댓값을 day로 갱신하며 최댓값 찾기
        day = max(day, max(row)) 

# 처음 시작을 0이 아닌 1부터 했으므로 -1을 해야 날짜를 구할 수 있음 
print(day-1)