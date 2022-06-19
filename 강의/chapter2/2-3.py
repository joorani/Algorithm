'''
k번째 큰 수
10 3
13 15 34 23 45 65 33 11 26 42
'''

#입력
n, k = map(int,input().split())
cards = list(map(int, input().split()))

sumList = set()
for i in range(n):
  for j in range(i+1,n):
    for m in range(j+1, n):
      sumList.add(cards[i]+cards[j]+cards[m])

sumList = list(sumList) #set자료구조는 sort 기능 없음
sumList.sort(reverse=True)
print(sumList[k-1])

