'''
6.22(수)
창고정리(그리디)

10
69 42 68 76 40 87 14 65 76 81
50
'''

n = int(input())
boxs = list(map(int, input().split()))
m = int(input())

boxs.sort()
for _ in range(m):
    boxs[0] += 1
    boxs[n-1] -= 1
    boxs.sort()

print(boxs[n-1]-boxs[0])
