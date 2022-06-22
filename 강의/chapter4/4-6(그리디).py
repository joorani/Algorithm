'''
6.22(수)
씨름 선수(그리디)

* 문제풀이 방법
- 키 내림차순으로 정렬
- maxWeight를 정하고 for문을 돌면서 갱신하여 확인
  갱신되면 cnt += 1

5
172 67
183 65
180 70
170 72
181 60

'''

n = int(input())
volunteers=[]
for _ in range(n):
    h, w = map(int, input().split())
    volunteers.append((h, w))

# 키 순으로 내림차순 정렬
volunteers.sort(reverse=True)

cnt = 0
maxWeight = 0
for h, w in volunteers:
    if w > maxWeight:
        cnt += 1
        maxWeight = w

print(cnt)


