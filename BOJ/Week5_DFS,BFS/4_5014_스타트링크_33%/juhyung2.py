from collections import deque
import sys

f, s, g, u, d = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(f+1)]


def bfs():
  queue = deque()
  queue.append(s)

  visited[s] = 1

  while queue:
    y = queue.popleft()

    if y==g:
      return visited[y] - 1
    else:
      for x in (y+u, y-d):
        if (0<x<=f) and visited[x]==0:
          visited[x] = visited[y] + 1
          queue.append(x)

  return "use the stairs"


print(bfs())