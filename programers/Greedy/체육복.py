'''

7.15(금)
체육복


-번호는 체격순 
-바로 앞이나 뒤에게만 빌려줄 수 있다.
-최대한  많은 학생
'''

from collections import deque
n = 5
lost = [2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    #여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있는 경우
    lost_s = set(lost)-set(reserve)
    reserve_s = set(reserve) - set(lost)

    for i in reserve_s:
        f = i-1
        b = i+1
        if f in lost_s:
            lost_s.remove(f)
        elif b in lost_s:
            lost_s.remove(b)
    return n - len(lost_s)
