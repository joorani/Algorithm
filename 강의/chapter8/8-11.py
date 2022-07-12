'''
동전교환(냅색 알고리즘)
6-7 문제와 같음. (DFS로 풀음)

3
1 2 5
15

제한있는 큰 값으로 초기화해야한다.
'''
n = int(input())
coins = list(map(int, input().split()))
m = int(input())

dy = [1000]*(m+1)
dy[0] = 0 #0을 넣어주고 해야함.
for coin in coins:
    for j in range(coin, m+1):
        dy[j] = min(dy[j], dy[j-coin]+1)
print(dy[m])


