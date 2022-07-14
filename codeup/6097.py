'''
6097 : [기초-리스트] 설탕과자 뽑기(py)

'''

h, w = map(int, input().split()) #격자 가로,세로
res = [[0] * (w+1) for _ in range(h+1)]
n = int(input()) #막대의 개수
for _ in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0: #방향이 가로 일때
        for i in range(y, y+l):
            res[x][i]= 1
    else:
        for j in range(x, x+l):
            res[j][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(res[i][j], end=' ')
    print()



