'''
7.11(월)
최대 선 연결하기(LIS 응용)
10
4 1 2 3 9 7 5 6 10 8
'''

n = int(input())
a = list(map(int, input().split()))

a.insert(0,0)

dy = [0]*(n+1)
res = 0
dy[1] = 1
for i in range(2, n+1):
    MAX=0
    for j in range(i - 1, 0, -1):  # 거꾸로 돌면서 확인
        if a[j] < a[i] and dy[j] > MAX:
            MAX = dy[j]
    dy[i] = MAX + 1
    if dy[i] > res:
        res = dy[i]
print(res)

