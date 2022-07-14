'''
7.13(수)
위상정렬(그래프 정렬)
6 6
1 4
5 4
4 3
2 5
2 3
6 2
'''
from collections import deque
n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
work = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    work[b] += 1

dq = deque()
for i in range(1, n+1):
    if work[i] == 0:
        dq.append(i)

while dq:
    x = dq.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
        if graph[x][i] == 1:
            work[i] -=1
            if work[i] == 0:
                dq.append(i)
