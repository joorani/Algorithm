'''
게임개발

- 현재 방향을 기준으로 왼쪽부터 시작해서 방향을 정한다.
- 왼쪽방향을 아직 가보지 않았다면 왼쪽으로 회전한 다음 왼쪽으로 한칸 전진
- 왼쪽방향에 가보지 않은 칸이 없다면


4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''


n, m = map(int, input().split())
A, B, direction = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for x in board:
    print(x)
#1은 바다, 0은 육지를 의미. 이동은 육지만 가능
#북, 동, 남, 서 방향
dx = [-1, 0, 1, 0]
dy =[0, 1, 0, -1]

#왼쪽방향으로 회전 (왼쪽방향으로 회전한다는 것은 방향이 북 -> 서 로 회전한다는 것을 의미한다)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


#시뮬레이션 시작
cnt = 1
direction_four = 0
board[A][B] = 1 #현재 좌표 방문 처리
while True:
    #왼쪽으로 회전
    turn_left()
    xx = A + dx[direction]
    yy = B + dx[direction]

    #방향이 맵을 벗어나는 경우는 무시
    if xx <0 or xx >= n or yy <0 or yy >= m:
        continue

    # 아직 가보지 않은 칸인 경우에는 회전 후 한칸 전진
    if board[xx][yy] == 0:
        A, B = xx, yy
        cnt += 1
        board[xx][yy] = 1
        direction_four = 0
        continue
    #네 방향 칸 모두 1인 경우이거나 바다로 되어 있는 칸인 경우
    else:
        direction_four += 1

    if direction_four == 4:
        bx = A - dx[direction]
        by = B - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if board[bx][by] == 0:
            A, B = bx, by
        else:
            break
        direction_four = 0


print(cnt)
