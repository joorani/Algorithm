'''

7.10(일)
토마토(BFS활용)
6 4
0 0 -1 0 0 0
0 0 1 0 -1 0
0 0 -1 0 0 0
0 0 0 0 -1 1

답
4

'''
from collections import deque
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
day = 0
dq = deque()
dis = [[0]*m for _ in range(n)]
#
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            dq.append((i, j))

while dq:
    tmp = dq.popleft()
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]
        if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 0:
            board[xx][yy] = 1 #익은토마토로 변경
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
            dq.append((xx, yy))
flag = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            flag = 0
result = 0
# board에 0이 없을 때 날짜 찾아서 리턴
if flag == 1:
    for i in range(n):
        for j in range(m):
            if dis[i][j] > result:
                result = dis[i][j] #dis 돌면서 최대값 찾기
    print(result)
else:
    print(-1)

