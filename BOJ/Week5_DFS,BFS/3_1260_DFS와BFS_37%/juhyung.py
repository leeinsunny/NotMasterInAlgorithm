from collections import deque
N,M,V = map(int, input().split())

#(N+1) x (N+1)인 2차원 리스트
#graph = [[False]*(N+1) for _ in range(N+1)]
graph = []
for _ in range(N+1):
  row = [False]*(N+1)
  graph.append(row)

for _ in range(M):
  # a와 b 사이에는 간선이 존재하면 True, 양방향
  a,b = map(int, input().split())
  graph[a][b] = True
  graph[b][a] = True

visited1 = [False] * (N+1)
visited2 = [False] * (N+1)


def dfs(v):
  visited1[v] = True
  print(v,end=" ")
  for i in range(1,N+1):
    #만약 i값을 방문하지 않았고 v와 연결이 되어 있다면
    if  not visited1[i] and graph[v][i]:
      #해당 i 값으로 dfs를 돈다
      dfs(i)


def bfs(v):
  #q에 v를 삽입한다
  q = deque([v])
  visited2[v] = True
  #q가 빌때까지 돈다
  while q:
    #큐에 있는 첫번째 값을 꺼낸다
    v = q.popleft()
    print(v,end=" ")
    for i in range(1,N+1):
      #i가 방문되지 않았고 v와 i 간의 간선이 있을 때
      if not visited2[i] and graph[v][i]:
        q.append(i)
        visited2[i] = True


dfs(V)
print()
bfs(V)
