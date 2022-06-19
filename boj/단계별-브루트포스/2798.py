#파이썬 라이브러리 사용 - 조합(합을 구해야하기 떄문에 순열이 아닌 순서가 고려하지 않는 조합을 이용했다)
import time

#1.라이브러리 사용
from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split())) #여기서 3개 선택해

sum_list = []

combi_list = list(combinations(lst, 3))
for cards in combi_list:
    if sum(cards) <= M:
        sum_list.append(sum(cards))

print(max(sum_list))

#2. for문 사용
N, M = map(int, input().split())
lst = list(map(int, input().split()))

biggest_sum = 0
start_time = time.time()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if lst[i]+lst[j]+lst[k] > M:
                continue
            else:
                biggest_sum = max(biggest_sum, lst[i]+lst[j]+lst[k])


print(biggest_sum)
end_time = time.time()
print(f"time={end_time-start_time} ")