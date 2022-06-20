'''
6.20(월)
곳감(모래시계)

7
74 10 31 26 59 16 89
78 44 49 1 64 33 15
9 95 70 18 22 25 40
62 77 28 3 78 75 23
82 38 20 16 42 1 79
1 24 2 25 95 26 79
4 35 46 94 70 44 83
3
2 0 3
5 1 2
3 1 4

1304

'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    # 회전 명령
    h, d, k = map(int, input().split())
    if d == 0:  # 왼쪽방향일 때
        for _ in range(k):
            tmp = arr[h - 1].pop(0)
            arr[h - 1].append(tmp)
    else:  # 오른쪽이면
        for _ in range(k):
            tmp = arr[h - 1].pop()
            arr[h - 1].insert(0, tmp)

# 모래시계 모양으로 합 구하기
resultSum = 0
s = 0  # 시작점
e = n - 1  # 끝점
for i in range(n):
    for j in range(s, e + 1):
        resultSum += arr[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(resultSum)
