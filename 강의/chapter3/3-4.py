'''
6.19(일)
두 리스트 합치기
3
1 3 5
5
2 3 6 7 9
'''

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# result = a+b
# result.sort()

# 출력
# for x in result:
#     print(x, end= ' ')
#

# 강사풀이
# sort()함수를 쓰면 시간 복잡도 : nlogn
# 이미 정렬되어있다는 사실을 이용하면 n번만에 가능하다.

# 포인트 2개 이용
p1 = p2 = 0
c = []
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:  # a가 남은 경우
    c += a[p1:]
if p2 < m:  # b가 남은 경우
    c += b[p2:]
for x in c:
    print(x, end=" ")
