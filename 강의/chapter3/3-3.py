'''
6.19(일)
카드 역배치
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20
'''

cards = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b - a + 1) // 2):
        cards[a - 1 + i], cards[b - 1 - i] = cards[b - 1 - i], cards[a - 1 + i]

# 출력
for x in cards:
    print(x, end=' ')
