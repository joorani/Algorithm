'''
송아지 찾기(BFS: 상태트리탐색)
5 14


'''
from collections import deque
MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n,m = map(int, input().split())
ch[n] = 1 #시작점은 처음부터 사용하기 때문에 갔다왔다고 표시
dis[n] = 0
dQ = deque()
dQ.append(n) #시작점 큐에 넣어줌.
while dQ: #큐가 다 비워지면 종료
    now = dQ.popleft()
    if now == m:
        break
    for next in(now-1, now+1, now+5): #차례로 3바퀴 돌음
        if 0 < next <= MAX:
            if ch[next] == 0: #방문 안했을 때
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] +1

print(dis[m])



for i in (1, 3, 5):
    print(i)
