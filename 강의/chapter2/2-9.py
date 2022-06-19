'''
주사위 게임

3
3 3 6
2 2 2
6 2 5
'''

# numbers = list(map(int, input().split()))

#주어진 리스트에 같은 수가 몇 개인지 판단
# def sameCount(arr):
#     cnt = 0
#     tmp = arr[0]
#     num = 0
#     for i in range(1, len(arr)):
#         if tmp == arr[i]:
#             cnt += 1
#             num = arr[i] #같은 수가 하나도 없을 떄 같은 수가 나오는 부분을 안했다.
#         tmp = arr[i]
#     return cnt, num
#
# # 상금을 계산하는 함수
# def calculateMoney(cnt, num):
#     money = 0
#     if cnt == 2:
#         money = (10000+num)*1000
#     elif cnt == 1:
#         money = (1000+num)*100
#     else:
#         money = num*100
#
#     return money
#
# # 상금끼리 비교
#
# for x in range(int(input())):
#     maxMoney = 0
#     numbers = list(map(int, input().split()))
#     cnt, num = sameCount(numbers) #같은 수가 몇 개인지 확인
#     money = calculateMoney(cnt, num)
#     print(cnt, num)
#     print(money)
#     print()
#     # if money > maxMoney:
#     #     maxMoney = money


n = int(input())
res = 0 #초기화 할 떄는 for문 밖에 선언하기
for i in range(n):
    tmp = input().split()
    tmp.sort() #나중에 가장 큰 값이 필요하기 때문에 미리 정렬한다.
    a, b, c = map(int, tmp) #각각 변수로 선언하면 같은 수를 판단할 때 편해진다.

    if a==b and b==c:
        money = 10000+(a*1000)
    elif a == b or a == c:
        money = 1000+(a*100)
    elif b==c:
        money = 1000+(a*100)
    else:
        money = c * 100

    if money > res:
        res = money

print(res)