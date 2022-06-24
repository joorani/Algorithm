'''
6.24(금)
응급실 (queue)

* 문제풀이
1. pop한 숫자가 남아있는 숫자보다 큰지 작은지 확인해야한다.
3. popleft 한 값이 max 값보다 작으면 뒤로 append한다.

정렬해서 값으로 비교하면 같은 값이 여러 개인 경우에 조건에 맞지 않는다.
그렇다면 어떻게 할 수 있을까?
튜플 자료형으로 몇 번째 값인지 알 수 있게 하자.
(몇 번째, 위험도)

5 2
60 50 70 80 90
'''

n, m  = map(int, input().split())
patients = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
from collections import deque

que = deque(patients)

cnt = 0
while True:
    cur = que.popleft()
    #남은 que에서 하나라도 더 큰 값이 있다면 pop한 값 뒤로 append
    if any(cur[1]<x[1] for x in que):
        que.append(cur)
    #가장 큰 값인 경우
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
