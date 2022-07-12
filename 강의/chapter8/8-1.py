'''
7.11(월)
동적계획법

네트워크 선 자르기(Bottom-up)


'''

n = int(input())
dy = [0]*(n+1)
dy[1] = 1 #1m 자를 수 있는 경우의 수
dy[2] = 2 #2m 자를 수 있는 경우의 수

for i in range(3, n+1):
    dy[i] = dy[i-1]+dy[i-2]

print(dy[n])
