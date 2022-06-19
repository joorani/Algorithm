'''
대표값
10
45 73 66 87 92 67 75 79 75 80

'''
n = int(input())
scoreList = list(map(int, input().split()))

#평균구하기
avg = round(sum(scoreList)/n)

#평균과 가장 가까운 점수 찾기

# for i in scoreList:
#   if abs(i-avg) < minAbs:
#     minAbs = abs(i-avg)
#
# for j in scoreList:
#   if abs(j-avg) == minAbs:
#     arr.append(j)
#
# if len(arr) > 1:
#   print(scoreList.index(max(arr))+1)

# min=214700000
# min= max(scoreList)
for idx, x in enumerate(scoreList):
  tmp = abs(x-avg)
  if tmp < min:
    min = tmp
    score = x
    res = idx+1
  elif tmp==min: #값이 여러개일때
    if x > score:
      score = x
      res = idx+1

print(avg, res)
