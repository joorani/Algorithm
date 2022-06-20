'''
6.20(월)
격자판 최대합

10
75 79 6 72 40 72 28 43 64 19
97 71 12 48 64 95 64 40 38 24
52 17 58 64 13 37 38 5 30 36
43 30 15 8 13 21 81 29 79 33
20 4 31 24 93 60 61 19 9 88
12 33 30 4 38 62 98 34 65 33
37 26 6 60 82 57 49 85 66 67
93 4 29 67 65 96 5 27 39 87
16 52 8 7 56 19 8 53 52 93
87 55 58 84 61 92 3 74 66 34

3
1 2 3
5 10 2
3 3 3
'''

# ===== 입력=============
n = int(input())

# 2차원 리스트 입력
arr = [list(map(int, input().split())) for _ in range(n)]

maxSum = 0
# 각 행, 열의 합
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += arr[i][j]  # 각 행의 합
        sum2 += arr[j][i]  # 각 열의 합

    if sum1 > maxSum:
        maxSum = sum1
    if sum2 > maxSum:
        maxSum = sum2
sum1 = sum2 = 0

# 대각선의 합
# (0,0 ) (1, 1) (2,2)
# (2,0) (1, 1) (0,2)
for i in range(n):
    sum1 += arr[i][i]
    sum2 += arr[i][n - 1 - i]
if sum1 > maxSum:
    maxSum = sum1
if sum2 > maxSum:
    maxSum = sum2

print(maxSum)
