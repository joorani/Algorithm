'''

왕실의 나이트

'''

start_p = input() #a1
#x, y 좌표
x = int(start_p[1])
y = ord(start_p[0]) - 96
print(x, y)

cnt = 0
dir = [(1, 2), (-1, 2), (1, -2), (-1, 2), (2, -1), (2, 1), (-2, 1), (-2, -1)] #갈 수 있는 방향
board = [[0] * 9 for _ in range(9)]

for move in dir:
    xx = x + move[0]
    yy = y + move[1]
    if xx <= 0 or xx >= 9 or yy <= 0 or xx >= 9:
        continue
    cnt += 1
print(cnt)


