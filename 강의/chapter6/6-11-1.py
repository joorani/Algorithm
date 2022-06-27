'''
6.27(월)
수들의 조합(라이브러리로 풀기)

'''

import itertools as it

n, k = map(int, input().split())
a=list(map(int, input().split()))
m = int(input())
cnt = 0

#a 리스트에서 k개 뽑는 조합
for x in it.combinations(a, k):
    if sum(x) % m == 0:
        cnt += 1
print(cnt)
