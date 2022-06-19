# DFS 메서드 정의

def dfs(graph, v, visited):

    #현재 노드를 방문처리
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque

q = deque()
queue.append()
queue.popleft()