'''
7.13(수)

최대점수 구하기(냅색 알고리즘)
5 20
10 5
25 12
15 8
6 3
7 4

한 유형당 한개만 풀수 있다는 조건이 있으므로 가방문제와는 조금 다르다.
다이나믹 테이블 뒤에서 부터 진행하면 중복이 되지 않는다.

'''

n, m = map(int, input().split())
dy = [0] * (m+1)
for i in range(n):
    p, t = map(int, input().split())
    for j in range(m, t-1, -1): #뒤에서 부터 채우면서 진행하면 중복을 피할 수 있다.
        dy[j] = max(dy[j-t]+p, dy[j])

print(dy[m])



