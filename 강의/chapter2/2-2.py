'''
k번쨰 수

2
6 2 5 3
5 2 5 3 8 9
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15

'''

#입력
t = int(input())
for i in range(t):
  n, s, e, k = map(int, input().split())
  arr = list(map(int, input().split()))
  arr = arr[s-1:e]
  arr.sort()
  print()
  print("#%d %d " %(i+1, arr[k-1]),)


