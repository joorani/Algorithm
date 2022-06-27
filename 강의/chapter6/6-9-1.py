'''
6.27(월)
수열 추측하기
라이브러리로 풀기

4 16
'''

import itertools as it

n, f = map(int, input().split())
b = [1]*n #이항정리 담는 리스트
for i in range(1, n):
    b[i] = b[i-1]*(n-i)//i

a=list(range(1, n+1))
cnt= 0

#a의 있는 순열을 자동으로 구해줌
#모든 순열
# for tmp in it.permutations(a):
#     print(tmp)

# n개 뽑을 때
# for tmp in it.permutations(a, 3):
#     print(tmp)
#     cnt +=1
# print(cnt)
for tmp in it.permutations(a):
    sum = 0
    for L, x in enumerate(tmp):
        sum += (b[L] * x)
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break
