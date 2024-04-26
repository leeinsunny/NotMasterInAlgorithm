from collections import deque

N = int(input())
graph = [list(input() for _ in range(N))]
visited = [[0]*N for _ in range()]
ans = [0,0]

def bfs(x,y):
  q = deque()
  q.append((x,y))
  visited[x][y] = 1

  while q:
    x,y = q.popleft()
    dx, dy = [1,-1,0,0],[0,0,1,-1]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      #배열 범위 내 , 색깔 같고, 방문 안한 경우
      if 0 <= nx < n and 0 <= ny < n and graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
        visited[nx][ny] = 1
        q.append((nx,ny))

#정산인이 볼 때의 그룹 개수
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      bfs(i,j)
      ans[0] += 1

#적록색맹이 볼 때의 그룹 개수를 새기 위하여 초록색을 빨간색으로 바꿈
for i in range(N):
  for j in range(N):
    if graph[i][j] =='G':
      graph[i][j] = 'R'

#적록색맹인이 볼 때의 그룹 개수
visited = [[0]*N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      bfs(i,j)
      ans[1] += 1

print(''.join(map(str,ans)))

