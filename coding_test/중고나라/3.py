# from collections import deque
# dx = [0,0,-1, 1]
# dy = [1, -1, 0,0]
# def solution(board, c):
#
#      def move(x, y):
#          answer = 0
#          queue = deque()
#          queue.append(x, y)
#
#          while queue:
#              x, y = queue.popleft()
#              for i in range(4):
#                  nx = x + dx[i]
#                  ny = y + dy[i]
#                  if nx < 0 or ny <0 or nx >= 0 or ny >=n:
#                      continue
#
#                 if board[nx][ny] ==1:
#                     answer += c