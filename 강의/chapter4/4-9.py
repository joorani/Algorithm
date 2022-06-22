'''
2022.6.22(수)
증가수열 만들기(그리디)
5
2 4 5 1 3

'''
from _collections import deque
n = int(input())
a = list(map(int, input().split()))
print(a)

a = deque(a)
result = ''
res = []
lt = a.popleft()
rt = a.pop()
tmp = 0
i = 0
while a:
    print(f'lt = {lt}')
    print(f'rt = {rt}')
    print(f'tmp = {tmp}')
    if len(a) == 1:
        result += 'L'
        res.append(a.pop())
        break

    if tmp > lt and tmp > rt:
        break  # 끝
    elif rt < tmp < lt:  # lt가 더 큰경우
        result += 'L'
        res.append(lt)
        tmp = lt
        lt = a.popleft()
    elif lt < tmp < rt:  # Rt가 더 큰 경우
        result += 'R'
        res.append(rt)
        tmp = rt
        rt = a.pop()
    else:  # tmp보다 lt, rt 모두 큰 경우
        if lt < rt:
            result += 'L'
            res.append(lt)
            tmp = lt
            lt = a.popleft()
        else:
            result += 'R'
            res.append(rt)
            tmp = rt
            rt = a.pop()  #
    i += 1
print(result)
print(res)
print(i)
