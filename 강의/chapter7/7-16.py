'''
7.10(일)

사다리타기(DFS)


왼, 오 확인해서 1이면 왼,오로 이동
            0이면 위로 이동

check 배열 안 만들고 board를 1이 아닌 수로 변경해도 된다. 어차피 한 번 갔다오면 사용하지 않을거기 때문
'''

def DFS(x, y):
    #왼,오 먼저 확인
    # ch[x][y] = 1
    board[x][y] = 0
    if x == 0:
        print(y)
    #왼쪽 확인
    else:
        # if y-1 >= 0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
        #     DFS(x, y-1)
        # elif y+1 < 10 and board[x][y+1] ==1 and ch[x][y+1] == 0:
        #     DFS(x, y+1)
        # #위로 이동
        # else:
        #     DFS(x-1, y)

        if y-1 >= 0 and board[x][y-1] == 1:
            DFS(x, y-1)
        elif y+1 < 10 and board[x][y+1] ==1:
            DFS(x, y+1)
        #위로 이동
        else:
            DFS(x-1, y)

if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]
    for y in range(10):
        if board[9][y] == 2:
            DFS(9, y)
