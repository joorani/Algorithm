'''
다리 라는 stack
조건에 맞는 차 append()
다리 위에 차가 있을 경우




'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = [0] * bridge_length
    while queue:
        queue.pop()
        time += 1
        while truck_weights:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
    return time
bridge_length = 2
weight = 10
truck_weights=[7,4,5,6]
print(solution(bridge_length, weight, truck_weights))
