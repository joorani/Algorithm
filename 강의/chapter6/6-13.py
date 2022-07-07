'''
6.27(월)
경로 탐색(그래프 DFS)


5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5

'''
def DFS(s):
    global cnt
    if s == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        ch[s] = 1
        for i in range(1, n+1):
            if g[s][i] == 1 and ch[i] == 0: #방문 안했고 간선이 있는 경우만 가능
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = [[0] * (n+1) for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    #
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(g[i][j], end=' ')
        print()
    ch = [0]*(n+1)
    cnt = 0
    path = []
    path.append(1)
    DFS(1)
    print(cnt)
