'''
7.9(토)

미로탐색(DFS)
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 1 0
1 0 0 0 0 0 0
'''

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0<=mx<=6 and 0<=my<=6 and board[mx][my] == 0:
                board[mx][my] = 1
                DFS(mx, my)
                board[mx][my] = 0


if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)




