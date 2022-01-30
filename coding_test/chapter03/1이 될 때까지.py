#최대한 나누기를 많이 하는 것이 포인트
#1. n을 k로 나누었을 때 나머지가 0이면 나눈다.
#2. 나누어지지 않는다면 n에서 1을 뺀다.

n, k = map(int, input().split())
count = 0
#1. 처음 푼 방법

# while n != 1:
#     if n % k == 0:
#         n = n // k
#     else:
#         n = n - 1
#     count += 1
# print(count)


#2번째 방법
while True:
    #n이 k로 나누어 떨어지는 수가 될 때가지 빼기
    target = (n // k) * k
    count += n-target
    n = target
    #n이 k보다 작을 때(더 이상 나눌 수 없을 떄) 반복문 탈출
    if n < k:
        break
    #k로 나누기
    count += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
count += n -1
print(count )