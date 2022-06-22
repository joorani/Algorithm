'''
6.22(수)
마구간 정하기(결정알고리즘)

5 3
1
2
8
4
9
'''

def count(distance):
    cnt = 1
    start = a[0]
    for i in range(1, n):
        tmp = a[i]-start
        if tmp >= distance:
            cnt += 1
            start = a[i]

    return cnt

# 1. 입력받기
n, c = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()

# 2. 값이 가능한 범위 정하기
# 1~9
lt = 1
rt = a[n-1] #9

res = 0
while lt <= rt:
    mid = (lt + rt)//2
    if count(mid) >= c:
        res = mid
        lt = mid +1
    else: #큰 값들 날려준다
        rt = mid -1
print(res)
