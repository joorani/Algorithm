'''
7.12(화)
가장 높은 탑 쌓기
5
25 3 4
4 4 6
9 2 3
16 2 5
1 5 2
'''

n = int(input())
brick = []
for i in range(n):
    s, h, w = map(int, input().split())
    brick.append((s,h,w))
brick.sort(reverse=True)

print(brick)
res = brick[0][1]
dp= [0] * n
dp[0] = brick[0][1]
for i in range(1, n):
    MAX = 0
    for j in range(i-1, -1, -1):
        if brick[i][2] < brick[j][2] and dp[j] > MAX:
            MAX = dp[j]
    dp[i]=MAX+brick[i][1]
    res = max(res, dp[i])
print(res)


