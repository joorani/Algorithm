'''
6.19(일)
수들의 합
8 3
1 2 1 3 1 1 1 2
'''

n, m = map(int, input().split())
a = list(map(int, input().split()))
#
# sum = 0
# cnt = 0
# for i in range(n):
#     print(i)
#     sum += a[i]
#     print(f'sum = {sum}')
#     if sum == m:
#         cnt += 1
#         sum = 0
#         i -= 1
# print(cnt)


# 강사풀이
lt = 0
rt = 1

cnt = 0
#
# while lt < n and rt < n:
#     tot = 0
#     for i in range(rt):
#         tot += a[lt]
#         if tot < m:
#             rt += 1
#         elif tot == m:
#             cnt+=1
#             tot -= a[lt]
#             lt+=1
#         else:
#             lt += 1

tot = a[0]
while True:
    if tot< m:
        if rt <n:
             tot += a[rt]
             rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)
