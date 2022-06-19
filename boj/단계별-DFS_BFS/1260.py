import collections

def dfs(v, visited = []):
    visited.append(v)



#정점 개수 n, 간선 개수 m, 탐색을 시작할 정점 번호 v
n, m, v = map(int,input().split())

#입력으로 주어지는 간선 양방향
graph = collections.defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
