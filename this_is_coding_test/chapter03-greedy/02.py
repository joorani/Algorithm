'''
큰 수의 법칙

5 8 3
2 4 5 4 6
'''
import time

start_time = time.time()
n,m,k = map(int, input().split()) #5, 8, 3
a = list(map(int, input().split())) #2, 4, 5, 4, 6
'''
a.sort(reverse=True) #내림차순으로 정렬
res = [0] * m #답을 담을 배열
# res = []
cnt = 0
for i in range(m):
    if cnt == k:
        res[i] = a[1]
        cnt = 0
    else:
        res[i] = a[0]
        cnt += 1
print(sum(res))

end_time = time.time()
print(f'time = {end_time-start_time}')
'''

#반복되는 수열을 이용한 방법
'''
가장 큰 수 : 6
두 번쨰로 큰 수 : 5
6+6+6+5+6+6+6+5 이런식으로 반복되면서  6+6+6+5라는 수열이 반복된다.
 
'''
a.sort()
first = a[n-1]
second = a[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m % (k+1) # m이 k+1로 나누어 떨어지지 않는 경우 가장 큰수가 추가로 더해지는 경우 고려.

res = 0
res += (count * first)
res += (m-count) * second

print(res)

