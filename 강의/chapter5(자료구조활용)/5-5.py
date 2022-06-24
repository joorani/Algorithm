'''
6.24(금)

공주 구하기(큐 자료구조로 해결)

* 문제 풀이방법
1. k이전 수는 pop해서 뒤에 다시 append
2. k번째 수는 pop
3. 마지막 한 명 남을 때까지 반복

8 3
'''
from collections import deque

n, k = map(int, input().split())
#list 초기화 방법 2가지 있음
# a = [x for x in range(1, n+1)]
a = list(range(1, n+1))
#queue 로 사용할 수 있게 deque 이용
a = deque(a)

cnt = 1
while len(a) > 1:
    #pop하고 뒤로 append
    if cnt != k:
        a.append(a.popleft())
        cnt += 1
    #pop만 하는 경우 : k번쨰
    else:
        a.popleft()
        cnt = 1

print(a[0])

#강사풀이
while a:
    for _ in range(k-1):
        a.append(a.popleft())
    a.popleft()
    if len(a) == 1:
        print(a[0])
        break

