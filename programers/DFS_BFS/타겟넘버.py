'''
7.18(월)
DFS

'''
def solution(numbers, target):
    cnt = 0
    def DFS(L, sum):
        nonlocal cnt
        # numbers를 다 돌면 무조건 종료해야함.
        if L == len(numbers):
            if sum == target:
                cnt += 1
        else:
            DFS(L+1, sum+numbers[L]) #더하는 경우
            DFS(L+1, sum-numbers[L]) #빼는 경우

    DFS(0,0)
    return cnt
numbers=[1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
