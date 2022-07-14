'''
6098 : [기초-리스트] 성실한 개미(py)
'''
import sys

board = [list(map(int, input().split())) for _ in range(10)]

#개미는 (2,2)에서 출발
sx=sy=1
for i in range(sx,10):
    for j in range(sy,10):

        if board[i][j] == 0:
            board[i][j] = 9
            sy = j
        else:
            break

    if board[i][j] == 2:
        board[i][j]=9
        break

for i in range(10):
    for j in range(10):
        print(board[i][j], end =' ')
    print()

