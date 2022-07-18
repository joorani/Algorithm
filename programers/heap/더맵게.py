'''

'''
import heapq

def solution(scoville, K):
    #주어진 리스트 heap으로 변경
    heapq.heapify(scoville)
    cnt = 0
    #최소힙이기 때문에 가장 작은 값이 k 이상이면 모든 값이 k 이상임.
    while scoville[0]<= k:
        if len(scoville) == 1:
            return -1
        #모든 음식의 지수를 k 이상으로 만들 수 없는 경우
        first = heapq.heappop(scoville) #가장 맵지 않은 음식
        second = heapq.heappop(scoville)
        tmp = first + (second * 2)
        cnt += 1
        heapq.heappush(scoville, tmp)


    return cnt


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k ))
