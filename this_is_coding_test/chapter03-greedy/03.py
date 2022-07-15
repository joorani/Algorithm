'''
숫자 카드 게임
3 3
3 1 2
4 1 4
2 2 2
'''

n,m  = map(int, input().split())
# cards=[list(map(int, input().split())) for _ in range(n)]
# print(cards)
#
# res = min(cards[0])
# for i in range(1, n):
#     tmp = min(cards[i])
#     if res <tmp:
#         res = tmp
# print(res)
res = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    res = max(res, min_value)

print(res)
