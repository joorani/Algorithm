'''
7.11(월)
최대 부분 증가수열(LIS)

dy 배열을 만들고 dy[i]에 수열에 i에 해당하는 값을 가장 마지막 값으로 가지는 수열의 가장 긴 값을 저장한다.
8
5 3 7 8 6 2 9 4
'''


# 1번 방법 DP. 시간복잡도 n^2
# n = int(input())
# a = list(map(int, input().split()))
#
# a.insert(0,0)
# dy = [0]*(n+1)
# res = 0
# dy[1] = 1
# for i in range(2, n+1):
#     MAX = 0
#     for j in range(i-1, 0, -1): #거꾸로 돌면서 확인
#         if a[j] < a[i] and dy[j] > MAX:
#             MAX = dy[j]
#     dy[i] = MAX+1
#     if dy[i] > res:
#         res = dy[i]
# print(res)

#2번 방법 이분탐색 이용 , 시간 복잡도 nlogn
import bisect

n = int(input())
a = list(map(int, input().split()))#5,2,7,8,6,2,9,4

dy = [a[0]] #5


for i in range(n):
    print(f'i = {i}, {a[i]}')
    if a[i] > dy[-1]: #현재 위치가 이전위치의 원소들보다 크면 dy에 추가
        dy.append(a[i])
        print(f'1번 dy = {dy}')
    else:
        idx = bisect.bisect_left(dy, a[i])
        print(f'idx = {idx}')
        dy[idx] = a[i]
        print(f'2번 dy = {dy}')
        print()

print(len(dy))
#
#
# #3번 풀이(수열을 직접 구할 때)
# n = int(input())
# a = list(map(int, input().split()))#5,2,7,8,6,2,9,4
# #3, 5, 7, 9, 2, 1, 4, 8
import sys, bisect
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
inc_arr = [sys.maxsize]*n


for i in range(0,n):
    idx = bisect.bisect_left(inc_arr, arr[i])
    inc_arr[idx] = arr[i]
    print(inc_arr)
print(bisect.bisect_left(inc_arr, sys.maxsize))
