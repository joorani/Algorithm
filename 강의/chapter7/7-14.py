'''

7.10(일)
안전영역(DFS)
5
71 24 70 91 17
85 66 42 46 56
81 44 63 57 69
87 13 53 49 15
5 58 15 86 100
'''

import sys

sys.setrecursionlimit(10 ** 5)  # 재귀
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# DFS

# def DFS(x, y, h):
#     ch[x][y] = 1
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0 <= xx < n and 0 <= yy < n and board[xx][yy] > h and ch[xx][yy] == 0:
#             DFS(xx, yy, h)
#
# if __name__ == '__main__':
#     n = int(input())
#     board = [list(map(int, input().split())) for _ in range(n)]
#     res = 0 #최종값 최대개수
#     for height in range(100): #100은 할 필요 없음 100인 경우 다 잠기기 때문에 안전영역은 0개가 된다
#         ch = [[0] * n for _ in range(n)]
#         cnt = 0#높이별로 매번 cnt
#         for i in range(n):
#             for j in range(n):
#                 if ch[i][j] == 0 and board[i][j] > height:
#                     cnt += 1
#                     DFS(i,j, height)
#
#         res = max(res, cnt) #최대값
#         if cnt == 0:
#             break #cnt = 0이라는 것은 height가 맥스값에 도달한 경우이므로 멈춰준다.
#     print(res)

# BFS
from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
Q = deque()
res = 0
for height in range(1, 101):
    cnt = 0
    ch = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > height and ch[i][j] == 0:
                ch[i][j] = 1
                Q.append((i, j))
                while Q:
                    tmp = Q.popleft()
                    for k in range(4):
                        x = tmp[0] + dx[k]
                        y = tmp[1] + dy[k]
                        if 0 <= x < n and 0 <= y < n and board[x][y] > height and ch[x][y] == 0:
                            Q.append((x, y))
                            ch[x][y] = 1
                cnt += 1
    res = max(res, cnt)
print(res)
