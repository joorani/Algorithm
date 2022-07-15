'''
1이 될 때까지

* 무조건 나누기를 많이하는게 최소 횟수가 된다.
25 5
'''

n, k = map(int, input().split())
cnt = 0
#n > k이상이라면 k로 계속 나누기
while n >= k:
    while n!=1:
        if n % k == 0:
            n = n//k
        else:
            n -= 1
        cnt += 1
print(cnt)
