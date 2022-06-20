'''
6.20(월)
사과나무(다이아몬드)

5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19


'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sum = 0
# for i in ran ge(n):
#   for j in range(n):
#     sum += arr[n//2][j]
#     sum += arr[j][n//2]
#
#
# for i in range(1, n-1):
#   for j in range(1, n-1):
#     sum += arr[i][j]
#
# print(arr[0][n//2])
# print(arr[n-1][n//2])
#
# print(arr[n//2][0])
# print(arr[n//2][n-1])

# =====강사풀이
# 포인터 2개 사용
s = e = n // 2
for i in range(n):
    for j in range(s, e + 1):
        sum += arr[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(sum)
