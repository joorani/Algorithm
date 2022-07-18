import math
from collections import deque
def solution(progresses, speeds):

    answer = []
    dq = deque()
    cnt = 0
    # 모든 작업의 작업일수를 계산하여 deque에 넣는다.
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        dq.append(day)
    print(dq)
    while dq:
        tmp = dq.popleft()
        cnt += 1
        # deque를 돌면서 pop한 수보다 작거나 같으면 pop한다.
        print(tmp)
        while dq and tmp >= dq[0]:
            dq.popleft()
            cnt += 1
        answer.append(cnt)
        cnt = 0

    return answer

#
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))
