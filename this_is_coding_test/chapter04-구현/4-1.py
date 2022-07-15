'''
상하좌우

5
R R R U D D
'''

n = int(input())
dir = list(input().split()) #방향 입력받기

board = [[0] * (n+1) for _ in range(n+1)]
x =y = 1

#이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for d in dir:
    for i in range(len(move)):
        if d == move[i]:
            xx = x + dx[i]
            yy = y + dy[i]
            if xx > n or xx < 1 or yy > n or yy < 1: #공간을 벗어나는 경우 무시
                continue
            x, y = xx, yy
print(x, y)
