'''
소수(에라토스테네스 체)

'''

'''
def isPrime(x):
  for i in range(2, x):
    if (x % i == 0 or x == 1):
      return False
  return True

n = int(input())
cnt = 0

for i in range(2, n):
  if isPrime(i):
    cnt += 1
print(cnt)
'''


#에라토스테네스의 체
n = int(input()) #입력
ch = [0] * (n+1)
primeCnt = 0
for i in range(2, n+1):
  if ch[i] == 0:
    primeCnt += 1
    for j in range(i, n+1, i):
      ch[j] = 1

print(primeCnt)
