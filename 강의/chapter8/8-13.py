'''
7.13(수)
플로이드 워샬 알고리즘

6 9
1 2 12
1 3 4
2 1 2
2 3 5
2 5 5
3 4 5
4 2 2
4 5 5
6 4 5

'''
n, m = map(int, input().split())

dy = [[5000] * (n+1) for _ in range(n+1)] #최대값으로 초기화
for _ in range(m):
    i, j, t = map(int, input().split())
    dy[i][j] = t
for i in range(1, n+1):
    dy[i][i] = 0

# *** 3중 for 문 플로이드 와샬 알고리즘 ***
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dy[i][j] = min(dy[i][k] + dy[k][j], dy[i][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dy[i][j] == 5000:
            print("M", end=" ")
        else:
            print(dy[i][j], end=' ')
    print()
