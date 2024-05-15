#1260 DFS와 BFS
import sys
import collections

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = collections.defaultdict(list)

for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

def dfs(vertex, visited):
    if vertex in visited:
        return
    visited.add(vertex)
    print(vertex, end=" ")

    for w in sorted(graph[vertex]):
        dfs(w, visited)

def bfs(start_vertex):
    visited = set([start_vertex])
    queue = collections.deque([start_vertex])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for w in sorted(graph[vertex]):
            if w not in visited:
                queue.append(w)
                visited.add(w)

dfs(V, set())
print()
bfs(V)