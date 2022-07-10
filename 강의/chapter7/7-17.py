'''
7.10(일)
피자 배달 거리(삼성 SW역량평가 기출문제 : DFS활용)
5 3
0 2 0 1 2
1 2 1 0 0
0 0 0 2 0
2 0 2 0 1
1 0 0 2 0


m개의 피자집을 조합으로 뽑은 후 각 집과의 거리를 계산하여 최소 피자배달 거리 출력
'''
def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for i in range(len(home)):
            x1 = home[i][0]
            y1 = home[i][1]
            dis = 2147000000
            for p in pz:
                x2 = pizza[p][0]
                y2 = pizza[p][1]
                dis = min(dis, abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum < res:
            res = sum

    else:
        for i in range(s, len(pizza)):
            pz[L] = i
            DFS(L+1, i+1)




if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    home = []
    pizza = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                home.append((i, j))
            elif board[i][j] == 2:
                pizza.append((i,j))
    pz= [0]*m
    res = 2147000000
    DFS(0, 0)



