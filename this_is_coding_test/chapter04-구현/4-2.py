'''
시각

24*60*60 하루가 86400초 이므로 100만개 하라 완전탐색으로 풀어도 된다.
'''

h = int(input())
count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k): #문자열에 3이 포함되어 있는지 확인한다.
                count+= 1

print(count)

