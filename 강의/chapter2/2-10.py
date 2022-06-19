'''
점수계산
10
1 0 1 1 1 0 0 1 1 0
'''

n = int(input())
arr = list(map(int, input().split()))
score = 0
result = 0
for i in arr:
    if i == 1:
        score += 1
        result += score
    else:
        score = 0


print(result)