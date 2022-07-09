'''
7.9(토)
섬나라 아일랜드(BFS)
5
0 0 0 0 0
1 0 0 1 1
0 1 0 1 0
1 1 0 1 0
1 1 0 0 0

대각선 방향도 고려해야함. 8방향 탐색
'''
from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
Q = deque()
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i,j))
            board[i][j] = 0
            while Q:
                tmp = Q.popleft()
                for z in range(8):
                    x = tmp[0]+dx[z]
                    y = tmp[1]+dy[z]
                    if x < 0 or x >= n or y <0 or y>= n or board[x][y] == 0:
                        continue
                    board[x][y] = 0
                    Q.append((x, y))
            cnt +=1

print(cnt)
