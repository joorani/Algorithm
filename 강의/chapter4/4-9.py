'''
2022.6.22(수)~23
증가수열 만들기(그리디)
5
2 4 5 1 3

'''
# from _collections import deque
# n = int(input())
# a = list(map(int, input().split()))
# print(a)
#
# a = deque(a)
# result = ''
# res = []
# lt = a.popleft()
# rt = a.pop()
# tmp = 0
# i = 0
# while a:
#     print(f'lt = {lt}')
#     print(f'rt = {rt}')
#     print(f'tmp = {tmp}')
#
#     if len(a) == 1:
#         result += 'L'
#         res.append(a.pop())
#         break
#
#     if tmp > lt and tmp > rt:
#         break  # 끝
#     elif rt < tmp < lt:  # lt가 더 큰경우
#         result += 'L'
#         res.append(lt)
#         tmp = lt
#         lt = a.popleft()
#     elif lt < tmp < rt:  # Rt가 더 큰 경우
#         result += 'R'
#         res.append(rt)
#         tmp = rt
#         rt = a.pop()
#     else:  # tmp보다 lt, rt 모두 큰 경우
#         if lt < rt:
#             result += 'L'
#             res.append(lt)
#             tmp = lt
#             lt = a.popleft()
#         else:
#             result += 'R'
#             res.append(rt)
#             tmp = rt
#             rt = a.pop()  #
#     i += 1
# print(result)
# print(res)
# print(i)

'''
강사풀이
'''
n = int(input())
a = list(map(int, input().split()))

#양 끝 값을 투 포인트로 지정
lt = 0
rt = n-1
tmp = 0
res = []
result = ''
while lt <= rt:
    if a[lt] > tmp:
        res.append((a[lt], 'L'))
    if a[rt] > tmp:
        res.append((a[rt],'R'))
    res.sort() #첫 자료값으로 정렬

    if len(res) == 0: # 종료조건
        break
    else:
        result = result+res[0][1]
        tmp = res[0][0]
        if res[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    res.clear()

print(len(result))
print(result)
