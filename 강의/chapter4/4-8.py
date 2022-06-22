'''
2022.6.22(수)
침몰하는 타이타닉(그리디)

5 140
90 50 70 100 60
'''
n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()

# cnt = n//2 if n % 2 == 0 else n//2+1
# sum = 0
# for i in range(0, n, 2):
#     # 짝수이면
#      if n%2 == 0:
#         sum = weights[i] + weights[i+1]
#         if sum > m:
#             cnt+=1
#     else:
#
cnt = 0
while weights:
    # 1명이 남았을 경우 처리가 필요함
    # 1명이 남았는데 pop을 할 경우 에러 생김
    if len(weights) == 1:
        cnt += 1
        break
    if weights[0] + weights[-1] > m:
        weights.pop()
        cnt += 1
    else:
        weights.pop(0) #인덱스로 pop할 경우 비효율적 연산이 시행된다. 시간복잡도 O(n)
        weights.pop()
        cnt += 1
print(cnt)


#2. deque 이용
from _collections import deque
weights = deque(weights)
while weights:
    if len(weights) == 1:
        cnt += 1
        break
    if weights[0] + weights[-1] > m:
        weights.pop()
        cnt += 1
    else:
        weights.popleft() #deque를 사용할 경우 시간복잡도 O(1)
        weights.pop()
        cnt+= 1
