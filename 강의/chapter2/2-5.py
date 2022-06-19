'''

정다면체

4 6
*풀이법
나올 수 있는 눈의 합에 대한 cnt list를 만들고 나올 때마다 cnt add해줌
'''

n, m = map(int, input().split())

cnt = [0] * (n+m+3)
for i in range(1, n+1):
  for j in range(1, m+1):
    cnt[i+j] += 1

#max 값 구하기
maxCnt = 0
for i in range(n+m+1):
  if cnt[i] > maxCnt:
    maxCnt = cnt[i]

#value가 max값인 index 리턴하기
for i in range(n+m+1):
  if cnt[i] == maxCnt:
    print(i, end=" ")
