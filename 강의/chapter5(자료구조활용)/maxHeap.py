'''
6.25(일)

최대힙


python에서 제공하는 heapq는 최소힙으로 작동하기 떄문에
heappush할 때 -를 붙여서 넣어준다.

5
3
6
0
5
0
2
4
0
-1

'''
import heapq as hq
a=[]
while True:
    n = int(input())
    if n == -1:
        break

    #꺼내어 출력하는 경우
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    #숫자가 입력되는 경우
    else:
        hq.heappush(a, -n)



