'''
7.12(화)

알리바바와 40인의 도둑(Bottom-up)

5
3 7 2 1 9
5 8 3 9 2
5 3 1 2 3
5 4 3 2 1
1 7 5 2 4
'''

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]* n for _ in range(n)]
dy[0][0] = board[0][0]
#dy의 양 0행 0열은 초기화해준다.
for k in range(1, n):
    dy[0][k] = dy[0][k-1]+board[0][k]
    dy[k][0] = dy[k-1][0]+board[k][0]

for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i][j-1], dy[i-1][j]) + board[i][j]
#
# for x in dy:
#     print(x)

print(f'답 = {dy[n-1][n-1]}')
