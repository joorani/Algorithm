'''
7.9(토)
단지 번호 붙이기(DFS, BFS)
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

'''

#DFS
'''


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for z in range(4):
        xx = x + dx[z]
        yy = y + dy[z]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            DFS(xx, yy)

if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt =0
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)
'''

# BFS로 풀기
from collections import deque

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
res = []
Q = deque()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 1
            Q.append((i, j))
            board[i][j] = 0
            while Q:
                tmp = Q.popleft()
                for z in range(4):
                    xx = tmp[0]+dx[z]
                    yy = tmp[1]+dy[z]
                    # if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
                    #     Q.append((xx, yy))
                    #     cnt += 1
                    #     board[i][j] = 0
                    if xx <0 or xx >= n or yy <0 or yy >=n or board[xx][yy] ==0:
                        continue
                    Q.append((xx, yy))
                    cnt += 1
                    board[xx][yy] = 0

            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)





