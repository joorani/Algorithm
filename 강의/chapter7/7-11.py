'''
7.9(토)

등산경로(DFS)
5
2 23 92 78 93
59 50 48 90 80
30 53 70 75 96
94 91 82 89 93
97 98 95 96 100

최소값, 최대값 인덱스 찾는 것이 관건

'''
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def DFS(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0 <= xx < n and 0<=yy<n and board[xx][yy] > board[x][y] and ch[xx][yy] == 0:
                ch[xx][yy] =1
                DFS(xx, yy)
                ch[xx][yy] = 0 #뺵할 때 풀어줘야된다. 체크 확인할 떄는 대칭구조로!!


if __name__ == '__main__':
    MIN = 2147000000
    MAX = -2147000000
    n = int(input())
    board = [[0] * n for _ in range(n)] # 등산경로 높이 저장
    ch = [[0] * n for _ in range(n)]

    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(n):
            if a[j] < MIN:
                MIN = a[j]
                sx = i
                sy = j
            if a[j] > MAX:
                MAX = a[j]
                ex = i
                ey = j
            board[i][j] = a[j]
    ch[sx][sy] = 1 #출발지 체크

    cnt = 0
    DFS(sx, sy)
    print(cnt)
