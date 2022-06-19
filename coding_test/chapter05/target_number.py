#프로그래머스 타겟 넘버

#1. dfs
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])

    while queue:
        temp, idx = queue.popleft()
        idx += 1

        if idx < n:
            queue.append([numbers[idx], idx])


