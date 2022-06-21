'''

6.21(화)
랜선자르기(결정알고리즘)
원하는 답이 특정 조건안에 있다.

1. 답의 범위는 1cm~802 사이로 정하고
2. 범위의 중간값이 답으로 가능한지 확인하는 작업을 한다.

4 11
802
743
457
539
'''

k, n = map(int, input().split())
lines = []
for i in range(k):
    lines.append(int(input()))

# 1. 답의 범위 정하기
lt = 1
rt = max(lines)
print(f'rt = {rt}')

# 2. 정답으로 가능한지 확인 -> 포인트 옮겨가면서 확인하기
def count(length):
    cnt = 0
    for x in lines:
        cnt += (x//length)

    return cnt

while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >= n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)
