'''
7.12(화)
가방문제(냅색 알고리즘)

4 11
5 12
3 8
6 14
4 8
'''

n, max_w = map(int, input().split())
dy = [0] * (max_w+1)

for i in range(n):
    weight, price = map(int, input().split())
    for j in range(weight, max_w+1):
        dy[j] = max(dy[j-weight]+price, dy[j])

print(dy[max_w])

