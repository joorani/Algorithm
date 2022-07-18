# '''
# 조이스틱
#
# 1. 상하로 이동하는 경우
#
#     1-1. a에서 z 방향으로
#     1-2. z에서 a 방향으로
#     찾아야하는 문자 인덱스가 어느 방향으로 했을 떄 더 최소로 움직일 수 있는 지를 계산해야한다.
# 2. 좌우로 이동하는 경우
#     2-1. 왼쪽에서 오른쪽으로만 이동하는 경우 문자열 길이-1
#     2-2. 'A'가 끼어있는 경우
# '''
# name="JEROEN"
# def solution(name):
#     cnt = 0 #정답
#     res = 'A'*len(name) #A로 초기화 AAAAAA
#     for i in range(len(name)):
#         #처음 문자열이 'A'인 경우
#         if name[0] == 'A':
#
#
#
#
#
# def up_or_down(index):
#     return min(ord('Z')- index +1, index)
#
# def getIndex(string):
#     return ord(string)-ord('A')
#
#
