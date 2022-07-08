'''
7.8(금)
3-7 문제랑 같은 문제

사과나무(BFS)

격자의 중심을 시작점으로 잡는다.
상하좌우로 트리를 뻗어 나간다.


5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
'''

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
sum = 0
Q = deque()
ch[n//2][n//2]=1
sum += a[n//2][n//2]
Q.append((n//2, n//2)) #격자의 가운데 부터 시작
L = 0
while True:
    if L == n//2:
        break
    size = len(Q) #처음 사이즈 1
    for i in range(size):
        tmp = Q.popleft() #처음 (2,2)
        for j in range(4):
            x = tmp[0]+dx[j]
            y = tmp[1]+dy[j]
            ch[x][y] = 1
            sum += a[x][y]
            Q.append((x, y))
    L += 1
print(sum)



