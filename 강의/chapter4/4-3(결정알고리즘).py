'''
6.22(수)
뮤직비디오(결정알고리즘)

9 3
1 2 3 4 5 6 7 8 9

'''

# 입력받기
n, m = map(int, input().split())
record = list(map(int, input().split()))

# 가능한 용량 크기 범위 설정
# x : record의 최대값 ~ sum(record)

# 하나의 음악을 나눠담을 수 없기 때문에 하나의 노래보다 커야한다.
lt = max(record)
rt = sum(record)
res = 0

def count(capacity):
    sum = 0
    cnt = 1
    for x in record:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= max(record) and count(mid) <= m:
        rt = mid - 1
        res = mid
    else:
        lt = mid + 1

print(res)
