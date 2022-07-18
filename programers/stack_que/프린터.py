'''

큐 이용
popleft()한 값보다 큰 값이 하나라도 있다면 뒤로 append()한다
pop()한 값이 큐에서 가장 큰 값이라면  cnt += 1
    찾고자 하는 값이라면 return
'''
from collections import deque
def solution(priorities, location):

    answer = 0
    dq = deque()
    for p, i in enumerate(priorities):
        dq.append((p, i))
    print(dq)

    while dq:
        tmp = dq.popleft()
        #pop한 값보다 큰 값이 있다면
        if any(tmp[1]< x[1] for x in dq):
            dq.append(tmp)
        #가장 큰 값인 경우
        else:
            answer += 1
            if tmp[0] == location:
                return answer


priorities = [2, 1, 3, 2]
location =2

t = solution(priorities, location)
print(t)
