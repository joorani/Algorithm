'''
7.9(토)

미로의 최단거리 통로(BFS)
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 1 0
1 0 0 0 0 0 0
'''
from collections import deque
board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]
# check 배열을 만들지 말고 주어진 board에서 이미 방문한 곳은 1로 만들어버리는 방법으로 해도 된다.

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
Q = deque()
Q.append((0, 0))
board[0][0] = 1 #이미 방문한 곳은 1로 만들어서 재방문 할 수 없도록 하기

while Q:
    tmp = Q.popleft()
    for j in range(4):
        x = tmp[0] + dx[j]
        y = tmp[1] + dy[j]
        if 0<=x<=6 and 0<=y<=6 and board[x][y] == 0:
            board[x][y] = 1 #이미 방문한 곳은 1로 만들어서 재방문 할 수 없도록 하기
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            Q.append((x, y))
    for x in dis:
        print(x)
    print()

if dis[6][6] == 0: #도착하지 못한 경우
    print(-1)
else:
    print(dis[6][6])