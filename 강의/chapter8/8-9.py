'''
7.12(화)

알리바바와 40인의 도둑(top-down)

5
3 7 2 1 9
5 8 3 9 2
5 3 1 2 3
5 4 3 2 1
1 7 5 2 4
'''

def DFS(x, y):
    if dy[x][y]>0:
        return dy[x][y]
    if x==0 and y==0:
        return board[0][0]
    else:
        if y==0:
            dy[x][y] = DFS(x-1, y)+board[x][y]

        elif x == 0:
            dy[x][y] = DFS(x, y-1)+board[x][y]
        else:
            dy[x][y] = min(DFS(x, y-1), DFS(x-1, y)) + board[x][y]
        return dy[x][y]


if __name__ == '__main__':

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]* n for _ in range(n)]
    print(DFS(n-1,n-1))
