# 1260 DFS와BFS

import sys
import collections

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = {}

for i in range(1, N + 1):
    graph[i] = []

for _ in range(M):
    S, E = map(int, input().split())
    graph[S].append(E)
    graph[E].append(S)


def DFS():
    result = []
    visited = set()

    def recursive(node):
        result.append(node)
        visited.add(node)
        for element in sorted(graph[node]):
            if element not in visited:
                recursive(element)

    recursive(V)
    return result


def BFS():
    result = []
    visited = set()
    queue = collections.deque()

    queue.append(V)
    visited.add(V)
    while queue:
        node = queue.popleft()
        result.append(node)
        for element in sorted(graph[node]):
            if element not in visited:
                queue.append(element)
                visited.add(element)
    return result


print(*DFS())
print(*BFS())
